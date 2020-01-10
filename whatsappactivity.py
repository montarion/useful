
import os, re, datetime
from time import sleep
#### MAKE IT LOOK STARTING FROM X DAYS AGO, 30 SHOULD BE FINE
###Variables!
names = []
dates = []
late = []
latedict = {}

fakereq = 14 
tht = -50
requirement = int(- + fakereq)
blacklist = ["names", "you", "don't", "want"]

###Colours
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

####Start
currentdate = datetime.datetime.now().strftime("%d/%m/%y")
#GET FRESH CHAT FILE FROM EMAIL FIRST
print("make sure you have a whatsapp group \"chat.txt\" file in a folder called \"waplogs\"")
input('please press enter to continue')
infile = open('waplogs/chat.txt', encoding='utf-8')
badchat = infile.readlines()
badchat.reverse()
infile.close()
outfile = open('waplogs/chat2.txt', 'w', encoding="utf-8")
for line in badchat:
    outfile.write(line)
outfile.close()


def lastseen(date):
    currentdate = datetime.datetime.now()
    lastactive = datetime.datetime.strptime(date, '%d/%m/%Y')
    difference = lastactive - currentdate
    inactivity = int(round(difference / datetime.timedelta(days=1)))
    return inactivity
print(WARNING + "requirement is for users to have said something in the last {} days.".format(fakereq))
sleep(2)
print("3...")
sleep(1)
print("2..")
sleep(0.8)
print("1.")
sleep(0.6)
print("let's  go.")
sleep(0.5)
with open('waplogs/chat2.txt', encoding="utf-8") as chat:
    for line in chat:
        #sleep(0.0001)

        search = "(.*?), (.*?) - (.*?)(\:)(.*?)"


        try:
            result = re.search(search, line)
            name = result.group(3)
            date = result.group(1)
            if "changed the subject from" not in name and name not in names and name not in blacklist:
                #print(WARNING + "processing message from: " + name + " " + date + ENDC)
                #print(OKGREEN + str(names) + ENDC)
                sleep(0.00001)
                if name[0] == '+':
                    name = name[1:]
                    if name not in names:
                        inactivity = lastseen(date)
                        if inactivity < requirement and inactivity > tht:
                            late.append(name)
                            names.append(name)
                            latedict.update({name: [date, inactivity]})
                            print(OKBLUE + 'processing ' + name + ENDC)
                            print(OKBLUE + str(name) + ENDC)
                        else:
                            print(OKGREEN + 'adding {}'.format(name) + ENDC)
                            names.append(name)
                            print(OKBLUE + 'processing ' + name + ENDC)
                else:
                    if name not in names:
                        inactivity = lastseen(date)
                        if inactivity < requirement and inactivity > tht:
                            late.append(name)
                            names.append(name)
                            latedict.update({name:[date, inactivity]})
                            print(OKBLUE + 'processing ' + name + ENDC)
                        else:
                            names.append(name)
                            print(OKBLUE + 'processing ' + name + ENDC)
        except AttributeError:
            continue


superfinallatelist = []
for line in late:
    try:
        final = RED + "{} has last been active at: {}, {} days ago.".format(line, latedict[line][0], str(latedict[line][1])[1:]) + ENDC
        print(final)
        latefile = open('latepeeps.txt', 'a')
        latefile.write("@{} ".format(line))
        latefile.close()
    except Exception as e:
        print(e)
        print("couldn't process: {}".format(line))


