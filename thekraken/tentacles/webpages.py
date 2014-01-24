# -*- coding: utf-8 -*-

import requests
from logbook import Logger

from thekraken.report import send_report
from thekraken.tentacles import Tentacle

log = Logger('thekraken.tentacles.webpages')


class WebpagesTentacle(Tentacle):

    def _check_element(self, element):
        """Checks a given webpage"""
        try:
            r = requests.get(element)
        except requests.exceptions.ConnectionError:
            log.error('Unable to connect to {0}'.format(element))
            send_report('[HTTP REQUEST ERROR] {0} (unable to connect)'.format(
                        element), '')
        except requests.exceptions.MissingSchema:
            log.error('No schema supplied for {0}'.format(element))
        else:
            if r.status_code == 200:
                log.debug('{0} sucessfuly requested'.format(element))
            else:
                log.error('{0} returns status {1}'.format(element,
                                                          r.status_code))
                send_report('[HTTP REQUEST ERROR] {0} '
                            '(unexpected status code)'.format(element),
                            'Returned status code {0}, expecting 200'.format(
                                r.status_code))
