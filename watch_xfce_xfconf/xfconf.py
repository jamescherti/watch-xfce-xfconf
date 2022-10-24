#!/usr/bin/env python
#
# Copyright (c) James Cherti
# URL: https://github.com/jamescherti/watch-xfce-xfconf/
#
# Distributed under terms of the MIT license.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""This command-line tool will help you to configure XFCE 4 programmatically.

It will display the xfconf-query commands of all the Xfconf settings that
are bring modified by xfce4-settings-manager (or by any other software that
modifies Xfconf like Thunar, Catfish, Ristretto...).

You can then add the xfconf-query commands to a Shell script that you can use
to configure XFCE 4 programmatically.

"""

import os
import signal
from pathlib import Path
from typing import Any, Set, Union
import pwd

import psutil
from lxml import etree as ETree

__author__ = "James Cherti"
__license__ = "MIT"


class XfconfError(Exception):
    """Exception raised by the class Xfconf() or its children."""


class XfconfItem:
    """Xfconf item."""

    def __init__(self,
                 channel: str,
                 property_path: str,
                 property_type: str,
                 property_value: Union[str, list]):
        """Init the class."""
        self.channel = channel
        self.property_path = property_path
        self.property_type = property_type
        self.property_value = property_value

    def __repr__(self) -> str:
        """Object representation in string format."""
        result = "{}{} : {} = {}".format(self.channel,
                                         self.property_path,
                                         self.property_type,
                                         self.property_value)
        return result


class Xfconf:
    """Load Xfconf settings."""

    @staticmethod
    def escape_command(command: str) -> str:
        """Quote a command."""
        return "'{}'".format(command.replace("'", "'\\''"))

    @staticmethod
    def reload_xfconfd():
        """Reload the process 'xfconfd'."""
        current_user = pwd.getpwuid(os.getuid()).pw_name
        for proc in psutil.process_iter():
            try:
                if proc.name() == "xfconfd":
                    if proc.username() == current_user:
                        # reload the process
                        os.kill(proc.pid, signal.SIGHUP)
            except psutil.Error:
                pass

    def __init__(self):
        """Load Xfconf settings."""
        self.xfconf_items: set = set()
        dir_xfconf = Path("~/.config/xfce4/xfconf/xfce-perchannel-xml")
        for xml_file in dir_xfconf.expanduser().glob("*.xml"):
            self._parse_xfconf_perchannel_xml(str(xml_file))

    def diff(self) -> Set[str]:
        """Return the settings that have been changed."""
        Xfconf.reload_xfconfd()

        new_xfce_config = Xfconf()

        before = set(str(self).splitlines())
        after = set(str(new_xfce_config).splitlines())

        self.xfconf_items = new_xfce_config.xfconf_items
        return after - before

    def __iter__(self):
        """Iterate through 'self.items'."""
        yield from self.xfconf_items

    def __repr__(self) -> str:
        """Object representation in string format."""
        commands = []

        for item in self:
            cmd = "{} --create -c {} -p {}" \
                .format("xfconf-query",
                        self.escape_command(item.channel),
                        self.escape_command(item.property_path))

            if item.property_type == "array":
                for array_item_type, array_item_value in item.property_value:
                    cmd =  "{} --type {} --set {}".format(
                        cmd,
                        self.escape_command(array_item_type),
                        self.escape_command(array_item_value)
                    )
            else:
                cmd =  "{} --type {} --set {}".format(
                    cmd,
                    self.escape_command(item.property_type),
                    self.escape_command(str(item.property_value))
                )

            commands.append(cmd)

        return "{}\n".format("\n".join(commands))

    def _parse_xfconf_perchannel_xml(self,
                                     xml_file: str,
                                     root: Any = None,
                                     channel_name: str = "",
                                     property_path: str = ""):
        """Parse the Xfconf XML."""
        if root is None:
            tree = ETree.parse(xml_file)
            root = tree.getroot()

            channel_name = root.attrib.get("name")
            if root.attrib.get("version") != "1.0" \
                    or root.tag.lower() != "channel":
                err_str = ("invalid XML file: '{}'").format(xml_file)
                raise XfconfError(err_str)

        for elem in root.getchildren():
            if elem.tag.title().lower() != "property":
                continue

            property_type = elem.attrib.get("type").strip().lower()
            cur_property_path = "{}/{}".format(property_path,
                                               elem.attrib.get("name").strip())

            if property_type not in ["empty", "uint", "int", "string", "bool",
                                     "array", "double"]:
                err_str = ("the type '{}' of '{}{}' is not supported. "
                           "XML file: '{}'") \
                    .format(property_type, channel_name, cur_property_path,
                            xml_file)
                raise XfconfError(err_str)

            # 'empty' = contains sub items
            if property_type == "empty":
                self._parse_xfconf_perchannel_xml(
                    xml_file=xml_file,
                    root=elem,
                    channel_name=channel_name,
                    property_path=cur_property_path
                )
                continue

            # Modify the variable property_value
            if property_type == "array":
                property_value = []
                for elem_property_value in elem.getchildren():
                    array_item_type = elem_property_value.attrib.get("type")
                    array_item_value = elem_property_value.attrib.get("value")
                    if array_item_value is None:
                        array_item_value = ""
                    property_value.append((array_item_type, array_item_value))
            else:
                property_value = elem.attrib.get("value")

            self.xfconf_items.add(
                XfconfItem(
                    channel=channel_name,
                    property_path=cur_property_path,
                    property_type=property_type,
                    property_value=property_value
                )
            )
