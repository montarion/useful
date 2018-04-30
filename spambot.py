import smtplib

i = 0
print("You should add your credentials!. comment this line and the one after it when you're done, like this:\n '#commented line")
exit() 
toaddrs = input("what address do you want to send it to?")
msg = input("what message do you want to send?")
counter = input("how often do you want to send your message")

while i < int(counter):
    

    username = 'username@gmail.com'
    password = 'password'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()

    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    i = i + 1

