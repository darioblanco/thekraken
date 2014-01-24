# -*- coding: utf-8 -*-

from thekraken.tentacles import machines
from thekraken.tests.tests import BaseTestCase


class TestMachines(BaseTestCase):

    def test_machine_is_up(self):
        """Should log success when a machine answers a ping request"""
        machine = 'google.com'
        mt = machines.MachinesTentacle([machine])
        mt.check()
        self.assertTrue("{0} machine ping successful".format(machine) in
                        self.log_handler.formatted_records)

    def test_machine_is_down(self):
        """Should log an error when unable to ping a machine"""
        machine = 'idontexistandiwillneverexistihope.com'
        mt = machines.MachinesTentacle([machine])
        mt.check()
        self.assertTrue("{0} machine ping failed".format(machine) in
                        self.log_handler.formatted_records)
