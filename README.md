# monitor-xfconf-changes - a command-line tool that can help you to configure XFCE 4 programmatically

The command-line tool monitor-xfconf-changes will display the xfconf-query commands of all the Xfconf settings that are being modified by XFCE programs like xfce4-settings-manager, thunar, catfish, ristretto...

You can then add the xfconf-query commands to a Shell script that you can use to configure XFCE 4 programmatically.

Configuring XFCE 4 programmatically is useful if you want to have the same XFCE 4 settings on several computers.

## Author
- [James Cherti](https://github.com/jamescherti/)

## Requirements

Python 3 requirements:
- psutil
- lxml
- mypy

## Usage

Clone the repository and enter the directory:
```console
$ git clone https://github.com/jamescherti/monitor-xfconf-changes/
$ cd monitor-xfconf-changes
```

Install the Python 3 requirements using pip:
```console
$ python3 -m pip install --user -r requirements.txt
```

Run xfce4-settings-manager in the background:
```console
$ xfce4-settings-manager &
```

Execute monitor-xfconf-changes:
```console
$ python3 ./monitor-xfconf-changes
[INFO] You can start modifying XFCE 4 settings with xfce4-settings-manager. Your changes will be displayed in this terminal...
```

## Features:
- Parse the XML files that are in the directory: "~/.config/xfce4/xfconf/xfce-perchannel-xml/",
- Monitor changes in XFCE 4 settings / Xfconf,
- Display xfconf-query commands,
- Supported Xfconf types: uint, int, string, bool, array, double.

## Links:
- The GitHub repository of 'monitor-xfconf-changes': https://github.com/jamescherti/monitor-xfconf-changes/
- More information about Xfconf: https://wiki.xfce.org/releng/4.6/general-info/
