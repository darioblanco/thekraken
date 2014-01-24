# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

from logbook import Logger

from thekraken.report import send_report
from thekraken.tentacles import Tentacle

log = Logger('thekraken.tentacles.machines')


class MachinesTentacle(Tentacle):

    def _check_element(self, element):
        """Pings a hostname"""
        ping = Popen(["ping", "-c", "2", element], stdout=PIPE, stderr=PIPE)
        out, error = ping.communicate()
        if error:
            log.error('{0} machine ping failed'.format(element))
            send_report('[PING ERROR] {0} (machine is down)'.format(element),
                        '')
        else:
            log.debug('{0} machine ping successful'.format(element))
