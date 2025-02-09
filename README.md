# watch-xfce-xfconf - Automate XFCE Configuration!
![License](https://img.shields.io/github/license/jamescherti/watch-xfce-xfconf)

## Introduction

The `watch-xfce-xfconf` command-line tool can be used to configure XFCE 4 programmatically. It displays the `xfconf-query` commands generated when XFCE 4 settings are modified, including settings for applications such as xfce4-settings-manager, Thunar, Catfish, Ristretto, and more.

The xfconf-query commands displayed by `watch-xfce-xfconf` allow modifying and creating XFCE 4 Xfconf settings, such as the desktop background, panel preferences, window decorations, window manager settings, and more.

By displaying the xfconf-query commands, `watch-xfce-xfconf` allows to easily create a Shell script that can be used to automate the configuration of XFCE 4, which provides several benefits:
- It saves time and effort by eliminating the need to manually adjust settings on each individual machine,
- It reduces the risk of errors and inconsistencies that may arise from manually configuring settings on different machines,
- Finally, it allows focusing on other important tasks rather than spending time configuring XFCE 4 manually.

The `watch-xfce-xfconf` tool is particularly useful for users who want to replicate XFCE 4 settings across different users or computers.

**Here is an example of an XFCE customization script created with the help of watch-xfce-xfconf: [jc-xfce-settings @GitHub](https://github.com/jamescherti/jc-xfce-settings).**

## Installation

To install the *watch-xfce-xfconf* executable locally in `~/.local/bin/watch-xfce-xfconf` using [pip](https://pypi.org/project/pip/), run:
```console
pip install --user watch-xfce-xfconf
```

(Omitting the `--user` flag will install *watch-xfce-xfconf* system-wide in `/usr/local/bin/watch-xfce-xfconf`.)

## Usage

Run xfce4-settings-manager in the background:
```console
xfce4-settings-manager &
```

After that, execute watch-xfce-xfconf:
```console
~/.local/bin/watch-xfce-xfconf
```

Once you begin modifying XFCE 4 settings using xfce4-settings-manager, `watch-xfce-xfconf` will automatically display the corresponding xfconf-query commands in the terminal. These xfconf-query commands can be easily copied and pasted into a Shell script, allowing for quick and efficient automation of XFCE 4 configuration across multiple machines.

## Author and License

The `watch-xfce-xfconf` tool has been written by [James Cherti](https://www.jamescherti.com/) and is distributed under terms of the MIT license.

## Features
- Parses XML files that are located in the directory: `~/.config/xfce4/xfconf/xfce-perchannel-xml/`,
- Monitors changes in XFCE 4 settings / Xfconf,
- Displays xfconf-query commands with correctly escaped special characters in their arguments.
- Reloads Xfconf when it is necessary.

## Links
- [watch-xfce-xfconf @PyPI](https://pypi.org/project/watch-xfce-xfconf/)
- [watch-xfce-xfconf @GitHub](https://github.com/jamescherti/watch-xfce-xfconf/)
- [General information about Xfconf](https://docs.xfce.org/xfce/xfconf/start)
