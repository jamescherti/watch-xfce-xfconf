#!/usr/bin/env python
"""A setuptools based setup module."""

from pathlib import Path
from setuptools import setup, find_packages

CURRENT_DIRECTORY = Path(__file__).parent.resolve()
LONG_DESCRIPTION = \
    (CURRENT_DIRECTORY / "README.md").read_text(encoding="utf-8")

setup(
    name="watch-xfce-xfconf",

    version="1.0.3",
    packages=find_packages(),

    description=("A command-line tool that can help you to configure XFCE 4 "
                 "programmatically"),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/jamescherti/watch-xfce-xfconf",
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
            "watch-xfce-xfconf=watch_xfce_xfconf.__init__:watch_xfce_xfconf",
        ],
    },
)
