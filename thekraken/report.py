# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.Utils import formatdate

from logbook import Logger

from thekraken.settings import MAIL

log = Logger('thekraken.report')


def send_report(subject, body):
    """Informs about an error"""
    msg = MIMEText(body, 'html', _charset='utf-8')

    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg['From'] = ', '.join(MAIL['sender'])
    msg['To'] = ', '.join(MAIL['recipients'])

    try:
        s = smtplib.SMTP(MAIL['smtp_server'])
    except:
        log.exception()
    else:
        try:
            s.login(MAIL['user'], MAIL['password'])
            s.sendmail(MAIL['sender'], MAIL['recipients'], msg.as_string())
        except:
            log.exception()
        finally:
            s.close()
