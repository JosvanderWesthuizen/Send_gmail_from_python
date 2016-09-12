# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

sender =     'me@gmail.com'
destination = ['recipient@her_email_domain.com']

PASSWORD = "PASSWORD_INTERNET_SERVICE_PROVIDER"

content="""\
Completed
"""

subject="Job 123"

import sys
import os
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']=       subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP('smtp.gmail.com')
    conn.set_debuglevel(False)
    conn.login(sender, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except Exception, exc:
    sys.exit( "mail failed; %s" % str(exc) ) # give a error message

print("Done")