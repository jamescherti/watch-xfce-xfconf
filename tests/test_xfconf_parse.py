#!/usr/bin/env python

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    import pwd  # noqa: F401
except ImportError:
    # xfconf_helpers imports pwd at module level (POSIX-only); stub it so
    # the parser tests can run on platforms without pwd (it is unused here).
    import types

    sys.modules["pwd"] = types.ModuleType("pwd")

from lxml import etree as ETree

from watch_xfce_xfconf.xfconf import Xfconf
from watch_xfce_xfconf.xfconf_item import XfconfError


def _parser():
    parser = Xfconf.__new__(Xfconf)
    parser.xfconf_items = set()
    return parser


def _channel(xml: str):
    return ETree.fromstring(xml)


def test_property_missing_type_raises_xfconf_error():
    root = _channel(
        '<channel name="test" version="1.0">'
        '<property name="foo" value="1"/>'
        "</channel>"
    )
    with pytest.raises(XfconfError):
        _parser()._parse_xfconf_perchannel_xml(
            "test.xml", root=root, channel_name="test", property_path=""
        )


def test_property_missing_name_raises_xfconf_error():
    root = _channel(
        '<channel name="test" version="1.0">'
        '<property type="string" value="1"/>'
        "</channel>"
    )
    with pytest.raises(XfconfError):
        _parser()._parse_xfconf_perchannel_xml(
            "test.xml", root=root, channel_name="test", property_path=""
        )


def test_valid_property_parses():
    root = _channel(
        '<channel name="test" version="1.0">'
        '<property name="foo" type="string" value="1"/>'
        "</channel>"
    )
    parser = _parser()
    parser._parse_xfconf_perchannel_xml(
        "test.xml", root=root, channel_name="test", property_path=""
    )
    assert len(parser.xfconf_items) == 1
