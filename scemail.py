import smtplib
import os
# from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(gmail_pass, send_from, send_to, subject, text, files=[]):
    """
    

    Parameters
    ----------
    gmail_pass : TYPE
        DESCRIPTION.
    send_from : TYPE
        DESCRIPTION.
    send_to : TYPE
        DESCRIPTION.
    subject : TYPE
        DESCRIPTION.
    text : TYPE
        DESCRIPTION.
    files : TYPE, optional
        DESCRIPTION. The default is None.
    

    Returns
    -------
    None.

    """
    assert isinstance(send_from, str)
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        fname = os.path.basename(f)
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(),
                                   Name=fname
                                   )
        # After the file is closed
        part['Content-Disposition'] = f'attachment; filename="{fname}"'
        msg.attach(part)
    #
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(msg['From'], gmail_pass)
    mailserver.send_message(msg)    
    mailserver.quit()
    print('Done')