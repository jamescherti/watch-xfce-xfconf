# watch-xfce-xfconf - Configure XFCE programmatically!

The command-line tool `watch-xfce-xfconf` will allow you to watch and display the `xfconf-query` commands of all the XFCE 4 / Xfconf settings that are being modified by XFCE programs like xfce4-settings-manager, thunar, catfish, ristretto...

You can then add the xfconf-query commands to a Shell script that you can use to configure XFCE 4 programmatically.

Configuring XFCE 4 programmatically is useful if you want to have the same XFCE 4 settings on several computers.

## Usage

Install the pip package from Github:
```console
sudo pip install watch-xfce-xfconf
```

Run xfce4-settings-manager in the background:
```console
xfce4-settings-manager &
```

Execute watch-xfce-xfconf:
```console
watch-xfce-xfconf
```

## Author
- [James Cherti](https://www.jamescherti.com/)

## Features
- Parse the XML files that are in the directory: "~/.config/xfce4/xfconf/xfce-perchannel-xml/",
- Monitor changes in XFCE 4 settings / Xfconf,
- Display xfconf-query commands,
- Supported Xfconf types: uint, int, string, bool, array, double.

## Links
- [watch-xfce-xfconf @PyPI](https://pypi.org/project/watch-xfce-xfconf/)
- [watch-xfce-xfconf @GitHub](https://github.com/jamescherti/watch-xfce-xfconf/)
- [General information about Xfconf](https://wiki.xfce.org/releng/4.6/general-info#xfconf)
