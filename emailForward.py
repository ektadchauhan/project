# The smtplib modules is useful for communicating with mail servers to send mail.
# SMTP stands for Simple Mail Transfer Protocol.
import smtplib

# To include a From, To and Subject headers, we should use the email package,
# since smtplib does not modify the contents or headers at all.
# Python's email package contains many classes and functions for composing and parsing email messages.
# Basically it contains the format to send the email.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SuccessEmail:
    # Composing some of the basic message headers:
    def __init__(self, fromaddr, toaddr):
        self.fromaddr = fromaddr
        self.toaddr = toaddr


    # Below line is to set up the correct format of the email we will be sending, like to, from, subject, body.
    # it gives the template of the email.
    def sendEmail(self,emailbody,sub):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = sub

        # Attaching the body of the email to the MIME message:
        msg.attach(MIMEText(emailbody, 'plain'))   # MIMEText allows to attach the body in the format you want, plain or html
        server = smtplib.SMTP('smtp.gmail.com',587)  # We open up the server, and specify the server we want to use and the port no.
        server.starttls()  # this will actually start it up and make sure everything is encrypted.
        server.login(msg['From'], '*****')    # provide the email and password to login
        server.sendmail(msg['From'], msg['To'], msg.as_string())    #actually send the msg by giving from and to details, and that msg is to be sent as string.
        server.quit()   # Ends our connection to the server.
        print("EMAIL SENT")







