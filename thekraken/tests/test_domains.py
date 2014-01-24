# -*- coding: utf-8 -*-

from thekraken.tentacles import domains
from thekraken.tests.tests import BaseTestCase


class TestDomains(BaseTestCase):

    def test_domain_resolve(self):
        """Should log success when a domain is resolved with the expected IP"""
        domain, ip = '8.8.8.8', '8.8.8.8'  # Forces a success
        dt = domains.DomainsTentacle([(domain, ip)])
        dt.check()
        self.assertTrue("Resolved {0} with ip {1}".format(domain, ip) in
                        self.log_handler.formatted_records)

    def test_domain_doesnt_exist(self):
        """Should log an error when a domain can't be resolved"""
        domain = 'idontexistandiwillneverexistihope.com'
        dt = domains.DomainsTentacle([(domain, '127.0.0.1')])
        dt.check()
        print self.log_handler.formatted_records
        self.assertTrue("Unable to resolve {0}".format(domain) in
                        self.log_handler.formatted_records)
