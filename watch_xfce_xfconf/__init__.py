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
"""This command-line tool will help you configure XFCE 4 programmatically."""

import sys
import time

from .xfconf import Xfconf

__author__ = "James Cherti"
__license__ = "MIT"


def watch_xfce_xfconf():
    """Command line interace of 'watch-xfce-xfconf'."""

    print("#!/usr/bin/env sh")
    print("# You can start modifying 'XFCE 4' settings with "
          "'xfce4-settings-manager'. Your")
    print("# changes will be displayed...\n")

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
