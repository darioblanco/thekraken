# -*- coding: utf-8 -*-

import dns.resolver
from logbook import Logger

from thekraken.report import send_report
from thekraken.tentacles import Tentacle

log = Logger('thekraken.tentacles.domains')


class DomainsTentacle(Tentacle):

    def _check_element(self, element):
        """Resolves a given domain"""
        domain, ip = element
        try:
            answers = dns.resolver.query(domain)
        except dns.resolver.NXDOMAIN:
            log.error('Unable to resolve {0}'.format(domain))
            send_report('[DNS ERROR] {0} (invalid domain)'.format(domain),
                        '')
        else:
            response = str(answers.response)
            if ip in response:
                log.debug("Resolved {0} with ip {1}".format(domain, ip))
            else:
                log.error('Resolved {0} with an unexpected ip'.format(domain))
                send_report('[DNS ERROR] {0} (unexpected IP)'.format(domain),
                            '<p>Expecting IP {0}.</p><p>Found: '
                            '</p><p>{1}</p>'.format(ip, response))
