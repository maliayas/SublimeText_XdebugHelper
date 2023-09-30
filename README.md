# XdebugHelper

XdebugHelper is a Sublime Text plugin that acts as a helper for the Sublime Text
plugin named [SublimeTextXdebug](https://github.com/martomo/SublimeTextXdebug).

## Overview

- [Requirements](#requirements)
- [Features](#features)
    - [`php.ini` Configuration For Xdebug](#phpini-configuration-for-xdebug)
    - [Hiding GitGutter During Debugging](#hiding-gitgutter-during-debugging)
* [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Todo](#todo)
- [License](#license)

## Requirements

Tested with Sublime Text Build 3125 and Xdebug 3.1.6

## Features

### `php.ini` Configuration For Xdebug

In order to debug PHP via Xdebug, some `php.ini` configuration needs to be done
manually. XdebugHelper does that automatically.

When a debugging session is started, `php.ini` file is automatically configured as:

```ini
[xdebug]
xdebug.mode = debug,profile
xdebug.start_with_request = yes
```

And when the session is stopped, `php.ini` file is reverted back to its original
state.

### Hiding GitGutter During Debugging

XdebugHelper will hide GitGutter during debugging in order to make SublimeTextXdebug
icons in the gutter visible. This feature applies only if the GitGutter plugin is
already installed.

## Installation

You can install the plugin via:

* Package Manager by searching `XdebugHelper`
* `git clone https://github.com/maliayas/SublimeText_XdebugHelper.git XdebugHelper`
* Downloading the [zip][] of the repo and extracting into `Packages/XdebugHelper`

## Configuration

You have to define the path of your `php.ini` file in your user settings. Multiple
paths are supported.

Open your user settings file via this menu:
`Preferences > Package Settings > Xdebug Helper`

## Usage

Usage is transparent. Normally, SublimeTextXdebug plugin starts a PHP debug session
via <kbd>Ctrl+Shift+F9</kbd> key binding and stops it via <kbd>Ctrl+Shift+F10</kbd>
key binding. XdebugHelper overrides these commands and works automatically once you
made the configuration.

## Todo

-   `xdebug.mode` can be made customizable.
-   Currently `xdebug.mode` and `xdebug.start_with_request` must already exist in
    your `php.ini` (their values don't matter). XdebugHelper only finds and modifies
    them. It would be more convenient to "add" them when they don't exist in the
    first place.

## License

XdebugHelper is released under the MIT License.

[zip]:  https://github.com/maliayas/SublimeText_XdebugHelper/archive/master.zip
