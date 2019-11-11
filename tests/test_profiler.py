# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0.  If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright 1997 - July 2008 CWI, August 2008 - 2016 MonetDB B.V.
"""
Tests for the profiler connection
"""


import unittest
from mock import patch
import pymonetdb
from tests import util


class ProfilerTest(unittest.TestCase):
    """Test the profiler connection."""

    @classmethod
    def setUpClass(cls):
        cls.conn = pymonetdb.profiler.ProfilerConnection()
        cls.conn.connect(**util.test_args)

    @patch('pymonetdb.mapi.Connection._getblock')
    def test_profiler_connection(self, mock_getblock):
        """Test opening a connection to the profiler"""
        response = '{"key":"value"}\n'  # A random JSON object
        mock_getblock.return_value = response
        self.assertEqual(self.conn.read_object(), response[:-1])

    @patch('pymonetdb.mapi.Connection.disconnect')
    def test_profiler_disconnect(self, mock_disconnect):
        """Test closing a profiler connection"""
        self.conn.disconnect()
        mock_disconnect.assert_called_once()
