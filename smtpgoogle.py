    sender='ykreddy8055@gmail.com'
    receiver=’yvreddy5317@gmail.com'
    password='9552783280'
    smtpserver=smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(sender,password)
    smtpserver.sendmail(sender,receiver,msg)
    print('Sent')
    smtpserver.close()
