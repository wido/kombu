from __future__ import absolute_import
from __future__ import with_statement

from mock import patch

from .. import transport
from .utils import unittest


class test_transport(unittest.TestCase):

    def test_resolve_transport__no_class_name(self):
        with self.assertRaises(KeyError):
            transport.resolve_transport("nonexistant")

    def test_resolve_transport_when_callable(self):
        self.assertTupleEqual(transport.resolve_transport(
                lambda: "kombu.transport.memory.Transport"),
                ("kombu.transport.memory", "Transport"))


class test_transport_gettoq(unittest.TestCase):

    @patch("warnings.warn")
    def test_compat(self, warn):
        x = transport._ghettoq("Redis", "redis", "redis")

        self.assertEqual(x(), "kombu.transport.redis.Transport")
        self.assertTrue(warn.called)