# -*- coding: utf-8 -*-

import unittest

from logbook import TestHandler


class BaseTestCase(unittest.TestCase):
    MOCKS = []

    def setUp(self):
        self.log_handler = TestHandler()
        self.log_handler.format_string = '{record.message}'
        self.log_handler.push_thread()

    def tearDown(self):
        self.log_handler.pop_thread()
