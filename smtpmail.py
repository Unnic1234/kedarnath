import smtplib
sender='ykreddy8055@gmail.com'
receiver='arathiyedhu@gmail.com'
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login('ykreddy8055@gmail.com','9552783280')
msg='hi'
smtpserver.sendmail('ykreddy8055@gmail.com','arathiyedhu@gmail.com','hi buddy')
print('Sent')
smtpserver.close()
