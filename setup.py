#!/usr/bin/env python
#
# Copyright (c) 2021, James Cherti
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
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""A setuptools based setup module."""

from pathlib import Path
from setuptools import setup, find_packages

CURRENT_DIRECTORY = Path(__file__).parent.resolve()
LONG_DESCRIPTION = (CURRENT_DIRECTORY / "README.md").read_text(encoding="utf-8")

setup(
    name="monitor_xfconf_changes",

    version="1.0.1",
    packages=find_packages(),

    description=("A command-line tool that can help you to configure XFCE 4 "
                 "programmatically"),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/jamescherti/monitor-xfconf-changes",
    author="James Cherti",

    python_requires=">=3.6, <4",
    install_requires=['mypy', 'psutil', 'lxml'],

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Environment :: X11 Applications",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Other",
        "Topic :: Desktop Environment :: Window Managers :: XFCE",
        "Topic :: Desktop Environment :: Window Managers",

        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],

    entry_points={
        "console_scripts": [
            "monitor-xfconf-changes=monitor_xfconf_changes.__init__:monitor_xfconf_changes",
        ],
    },
)
