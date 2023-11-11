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

from typing import Union

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
