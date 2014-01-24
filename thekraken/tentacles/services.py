# -*- coding: utf-8 -*-

import socket
from logbook import Logger

from thekraken.report import send_report
from thekraken.tentacles import Tentacle

log = Logger('thekraken.tentacles.services')


class ServicesTentacle(Tentacle):

    def _check_element(self, element):
        """Pings a service listening into a specific port"""
        hostname, port = element

        s = socket.socket()
        try:
            s.connect((hostname, port))
        except socket.error:
            log.error('Unable to connect to service {0}:{1}'.format(hostname,
                                                                    port))
            send_report('[SERVICE ERROR] {0}:{1} (service is down)'.format(
                        hostname, port), '')
        else:
            log.debug('{0}:{1} service check successful'.format(hostname,
                                                                port))
