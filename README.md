# watch-xfce-xfconf - XFCE 4 Configuration as Code
![License](https://img.shields.io/github/license/jamescherti/watch-xfce-xfconf)

The `watch-xfce-xfconf` monitors XFCE settings in real time and prints the corresponding `xfconf-query` commands whenever a setting is modified through the graphical interface.

Configuration changes performed in components such as `xfce4-settings-manager`, Thunar, Catfish, Ristretto, and other XFCE applications are translated into explicit `xfconf-query` commands. These commands reveal how XFCE 4 persists and applies configuration at the Xfconf layer.

The generated commands can be reused to modify or create XFCE 4 settings programmatically, including desktop backgrounds, panel layouts, window decorations, window manager behavior, and related preferences.

By displaying the xfconf-query commands, `watch-xfce-xfconf` allows to easily create a Shell script that can be used to automate the configuration of XFCE 4, which provides several benefits:
- It saves time and effort by eliminating the need to manually adjust settings on each individual machine,
- It reduces the risk of errors and inconsistencies that may arise from manually configuring settings on different machines,
- Finally, it allows focusing on other important tasks rather than spending time configuring XFCE 4 manually.

The `watch-xfce-xfconf` tool is useful for users who want to replicate XFCE 4 settings across different users or computers.

**Here is an example of an XFCE customization script created with the help of watch-xfce-xfconf: [jc-xfce-settings @GitHub](https://github.com/jamescherti/jc-xfce-settings).**

If *watch-xfce-xfconf* enhances your workflow, please show your support by **⭐ starring watch-xfce-xfconf on GitHub** to help more users discover its benefits.

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
