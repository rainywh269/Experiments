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

send_email('guohaochuan@gmail.com','','guohaochuan@gmail.com','sdfg','sd')
