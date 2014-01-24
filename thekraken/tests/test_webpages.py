# -*- coding: utf-8 -*-

from thekraken.tentacles import webpages
from thekraken.tests.tests import BaseTestCase


class TestWebpages(BaseTestCase):

    def test_webpage_status_200(self):
        """Should log success when a webpage was properly requested"""
        webpage = 'http://google.com'
        wt = webpages.WebpagesTentacle([webpage])
        wt.check()
        self.assertTrue("{0} sucessfuly requested".format(webpage) in
                        self.log_handler.formatted_records)

    def test_unable_to_connect_to_webpage(self):
        """Should log an error when unable to connect to a webpage"""
        webpage = 'http://idontexistandiwillneverexistihope.com'
        wt = webpages.WebpagesTentacle([webpage])
        wt.check()
        self.assertTrue("Unable to connect to {0}".format(webpage) in
                        self.log_handler.formatted_records)

    def test_webpage_without_schema(self):
        """Should log an error when the given webpage does not have a schema"""
        webpage = 'google.com'
        wt = webpages.WebpagesTentacle([webpage])
        wt.check()
        self.assertTrue("No schema supplied for {0}".format(webpage) in
                        self.log_handler.formatted_records)
