import sublime
import sublime_plugin
import importlib
import re


SETTINGS            = sublime.load_settings("Xdebug Helper.sublime-settings")
GITGUTTER_SETTINGS  = sublime.load_settings("GitGutter.sublime-settings")

ORIGINAL_XDEBUG_CONFIG = {}
ORIGINAL_GITGUTTER_SETTING = GITGUTTER_SETTINGS.get("git_binary")

INI_LINE_REGEX = r"(?m)^[ \t]*(%s)[ \t]*=[ \t]*(.*?)[ \t]*$"

GITGUTTER_INSTALLED = importlib.find_loader('GitGutter') is not None

class XdebugSessionStartWrapperCommand(sublime_plugin.WindowCommand):
    def run(self):
        Helper.enable_xdebug()

        if GITGUTTER_INSTALLED:
            Helper.disable_gitgutter()

        self.window.run_command("xdebug_session_start")

class XdebugSessionStopWrapperCommand(sublime_plugin.WindowCommand):
    def run(self):
        Helper.disable_xdebug()

        if GITGUTTER_INSTALLED:
            Helper.enable_gitgutter()

        self.window.run_command("xdebug_session_stop")

class Helper():
    def configure_php_ini(ini, xdebug_config, backup_original = False):
        global ORIGINAL_XDEBUG_CONFIG

        ini_content = open(ini).read()

        if backup_original:
            ORIGINAL_XDEBUG_CONFIG[ini] = {}

        for key, value in xdebug_config.items():
            if backup_original:
                match = re.search(INI_LINE_REGEX % re.escape(key), ini_content)
                ORIGINAL_XDEBUG_CONFIG[ini][key] = match.group(2) if match else None

            if value is not None:
                ini_content = re.sub(INI_LINE_REGEX % re.escape(key), r"\1 = " + value, ini_content)

        open(ini, "w").write(ini_content)

    def enable_xdebug():
        xdebug_config = {
            "xdebug.mode"               : "debug,profile",
            "xdebug.start_with_request" : "yes",
        }

        for ini in SETTINGS.get("php_ini_files"):
            Helper.configure_php_ini(ini, xdebug_config, True)

    def disable_xdebug():
        global ORIGINAL_XDEBUG_CONFIG

        for ini in SETTINGS.get("php_ini_files"):
            Helper.configure_php_ini(ini, ORIGINAL_XDEBUG_CONFIG[ini])

        ORIGINAL_XDEBUG_CONFIG = {}

    def configure_gitgutter(git_binary):
        if git_binary:
            GITGUTTER_SETTINGS.set("git_binary", git_binary)
        else:
            GITGUTTER_SETTINGS.erase("git_binary")

    def enable_gitgutter():
        Helper.configure_gitgutter(ORIGINAL_GITGUTTER_SETTING)

        # Trigger refreshing GitGutter.
        sublime.active_window().run_command("git_gutter")

    def disable_gitgutter():
        Helper.configure_gitgutter("disabled")

        # Remove GitGutter regions in order to quickly hide GitGutter.
        for region_name in ['deleted_top', 'deleted_bottom', 'deleted_dual', 'inserted', 'changed', 'untracked', 'ignored']:
            sublime.active_window().active_view().erase_regions('git_gutter_%s' % region_name)
