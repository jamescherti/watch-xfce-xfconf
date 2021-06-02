# monitor-xfconf-changes

The command-line tool monitor-xfconf-changes can help you to configure XFCE 4 programmatically.

It will display the xfconf-query commands of all the settings that are modified by any software that modifies Xfconf: xfce4-settings-manager, thunar, catfish, ristretto...

You can then add the xfconf-query commands to a Shell script that you can use to configure XFCE 4 programmatically.

Configuring XFCE 4 programmatically is useful if you want to have the same configuration on several XFCE 4 desktops.

## Author
- [James Cherti](https://github.com/jamescherti/)

## Requirements

Python 3 requirements:
- [psutil](https://pypi.org/project/psutil/)
- [lxml](https://pypi.org/project/lxml/)
- [mypy](https://pypi.org/project/mypy/)

## Usage

Clone the repository and enter the directory:
```console
$ git clone https://github.com/jamescherti/monitor-xfconf-changes/
$ cd monitor-xfconf-changes
```

Run xfce4-settings-manager in the background:
```console
$ xfce4-settings-manager &
```

Execute monitor-xfconf-settings.py:
```console
$ ./monitor-xfconf-settings.py
[INFO] You can start modifying XFCE 4 settings with xfce4-settings-manager. Your changes will be displayed in this terminal...
```

## Features:
- Parse the XML files that are in the directory: "~/.config/xfce4/xfconf/xfce-perchannel-xml/",
- Monitor changes in XFCE 4 settings / Xfconf,
- Display xfconf-query commands,
- Supported Xfconf types: uint, int, string, bool, array, double.

## Links:
- monitor-xfconf-changes GitHub repository: https://github.com/jamescherti/monitor-xfconf-changes/
- More information about Xfconf: https://wiki.xfce.org/releng/4.6/general-info/
