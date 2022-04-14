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
# --
# pylint: disable=invalid-name
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
import sys
import time
from pathlib import Path
from typing import Any, Set, Union

import psutil
from lxml import etree as ETree

from .xfconf import Xfconf

__author__ = "James Cherti"
__license__ = "MIT"


def watch_xfce_xfconf():
    """Command line interace of 'watch-xfce-xfconf'."""

    print("[INFO] You can start modifying 'XFCE 4' settings with "
          "'xfce4-settings-manager'. Your changes will be displayed in this "
          "terminal...\n", file=sys.stderr)

    try:
        xfconf_query_list = Xfconf()
        while True:
            time.sleep(1)
            delta = xfconf_query_list.diff()
            for item in delta:
                print(item)
            sys.stdout.flush()
    except KeyboardInterrupt:
        pass
