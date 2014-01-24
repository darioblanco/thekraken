# -*- coding: utf-8 -*-

import argparse
import os
import sys

from logbook import MonitoringFileHandler, NullHandler, StreamHandler

from thekraken.tentacles import domains, machines, services, webpages
from thekraken.settings import LOG_DIR, DOMAINS, MACHINES, SERVICES, WEBPAGES


def parse_arguments():
    """Parses console arguments"""
    parser = argparse.ArgumentParser(description='Release the Kraken!!!!!!')
    parser.add_argument("--quiet", action="store_true", default=False,
                        help="Don't show log info in the console")
    return vars(parser.parse_args())


def inject_logging(quiet):
    """Injects logging"""
    null_handler = NullHandler(level='DEBUG')
    null_handler.push_application()  # Discard any message lesser than INFO
    log_handler = MonitoringFileHandler(os.path.join(LOG_DIR, 'thekraken.log'),
                                        level='INFO')
    log_handler.push_application()
    if not quiet:
        console_handler = StreamHandler(sys.stdout, level='DEBUG', bubble=True)
        console_handler.push_application()


if __name__ == '__main__':
    """Summons the Kraken"""
    args_dict = parse_arguments()

    inject_logging(args_dict['quiet'])

    dt = domains.DomainsTentacle(DOMAINS)
    dt.check()
    mt = machines.MachinesTentacle(MACHINES)
    mt.check()
    st = services.ServicesTentacle(SERVICES)
    st.check()
    wt = webpages.WebpagesTentacle(WEBPAGES)
    wt.check()
