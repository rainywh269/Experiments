#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.MIMEText import  MIMEText
import smtplib

def send_email(user_email_address,user_password,target_addr,subject,body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = user_email_address
    msg['To'] = target_addr

    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(user_email_address,user_password)
    smtpObj.sendmail(user_email_address, [user_email_address], msg.as_string())         
    smtpObj.close()  

#send_email('guohaochuan@gmail.com','','guohaochuan@douban.com','sdfg','sd')

import smtplib

def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print "Enter message, end with ^D (Unix) or ^Z (Windows):"

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print "Message length is " + repr(len(msg))

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('guohaochuan@gmail.com','')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
