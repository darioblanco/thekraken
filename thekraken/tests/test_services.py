# -*- coding: utf-8 -*-

from thekraken.tentacles import services
from thekraken.tests.tests import BaseTestCase


class TestServices(BaseTestCase):

    def test_service_connected_success(self):
        """Should log success when a service could be pinged"""
        host, port = 'google.com', 80  # Forces a success
        st = services.ServicesTentacle([(host, port)])
        st.check()
        self.assertTrue(
            '{0}:{1} service check successful'.format(host, port) in
            self.log_handler.formatted_records
        )

    def test_service_connected_fail(self):
        """Should log an error when a service could not be pinged"""
        host, port = 'idontexistandiwillneverexistihope.com', 8000
        st = services.ServicesTentacle([(host, port)])
        st.check()
        self.assertTrue(
            'Unable to connect to service {0}:{1}'.format(host, port) in
            self.log_handler.formatted_records
        )
