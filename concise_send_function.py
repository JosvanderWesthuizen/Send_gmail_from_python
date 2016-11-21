from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

from email.mime.text import MIMEText

def send_mail(destination=['josvdwest@gmail.com'], subject="Subject", content="\nCompleted"):
    # SMTPserver = 'smtp.att.yahoo.com'
    sender = 'josvdwest@gmail.com'

    PASSWORD = "" #Your gmail password

    # typical values for text_subtype are plain, html, xml
    text_subtype = 'plain'

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

#Quickly test the function
send_mail(["josvdwest@gmail.com"])
print("Done")