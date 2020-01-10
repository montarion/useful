import smtplib, threading
from time import sleep
i = 0
print("You should add your credentials!. comment this line and the one after it when you're done, like this:\n '#commented line")
exit()
toaddrs = ["list", "of", "targets"]
msg = "Staakt en houdt gestaakt uw illegale protesten, blokkades, en andere acties die de openbare orde en veiligheid verstoren."
counter = input("how often do you want to send your message")

def sendmail(toaddrs, counter):
    i = 0
    username = 'username@gmail.com'
    password = 'supersecurepassword' # you will have to enable "insecure access" at https://myaccount.google.com/lesssecureapps
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    while i < int(counter):
        server.sendmail(username, toaddrs, msg)
        i = i + 1
        print("sent mail number {} to address: {}".format(i, toaddrs))
    server.quit()

t1 = threading.Thread(target=sendmail, args=(toaddrs[0], counter)).start()
t2 = threading.Thread(target=sendmail, args=(toaddrs[1], counter)).start()
t3 = threading.Thread(target=sendmail, args=(toaddrs[2], counter)).start()
