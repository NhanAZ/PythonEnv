import smtplib

user = 'username@gmail.com'
passworld = '12345678'

target = 'target@gmail.com'
msg = 'Hello World!'

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=user, password=passworld)

connection.sendmail(from_addr=user, to_addrs=target, msg=msg)

connection.close()
