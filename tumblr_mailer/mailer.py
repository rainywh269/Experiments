#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
mailer.py
Author: WooParadog
Email:  Guohaochuan@gmail.com

Created on
2012-05-01
'''
from configs import SMTP_PASSWORD, SMTP_USERNAME, SMTP
from model import Post 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
import smtplib
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from datetime import date

def send_mail(send_from, send_to, subject, text, attachment):
    assert type(send_to)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    part = MIMEBase('application', "octet-stream")
    part.set_payload(attachment)
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 
            'attachment; filename="%s.html"'% str(date.today()))
    msg.attach(part)

    smtp = smtplib.SMTP(SMTP)
    smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def main():
    result = []
    for i in Post.get_unmailed_posts():
        result.append(i.text)
        i.update_post_state()
    #text = '\n\n---\n\n'.join(result)
    text = ''.join(result)
    text = text.encode('utf8')
    addr = ["guohaochuan@kindle.com", "guohaochuan@gmail.com"]#"rainywh269@gmail.com"]
    send_mail(SMTP_USERNAME, addr,'sddd', 'asdfasdf', text)

if __name__ == '__main__':
    main()
