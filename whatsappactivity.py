import os, re, datetime
from time import sleep

###Variables!
names = []
dates = []
datedict = {}
late = []
latedict = {}
fakereq = 15
requirement = int(- + fakereq)

###Colours
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

####Start
currentdate = datetime.datetime.now().strftime("%d/%m/%y")
#GET FRESH CHAT FILE FROM EMAIL FIRST
#input('please press enter to continue')
infile = open('chat.txt', encoding='utf-8')
badchat = infile.readlines()
badchat.reverse()
infile.close()
outfile = open('chat2.txt', 'w', encoding="utf-8")
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
with open('chat2.txt', encoding="utf-8") as chat:
    for line in chat:
        #sleep(0.0001)

        search = "(.*?), (.*?) - (.*?)(\:)(.*?)"


        try:
            result = re.search(search, line)
            name = result.group(3)
            date = result.group(1)
            if "changed the subject from" not in name and name not in names:
                #print(WARNING + name + " " + date + ENDC)
                #print(OKGREEN + str(names) + ENDC)
                sleep(0.1)
                if name[0] == '+':
                    if name[1:-1] not in names:
                        if lastseen(date) < requirement:
                            late.append(name[1:-1])
                            names.append(name[1:-1])
                            latedict.update({name: date})

                            #print(RED + 'processing ' + name[1:-1] + ENDC)

                            #print(OKBLUE + str(name) + ENDC)

                        else:
                            #print('adding {}'.format(name[1:-1]))
                            names.append(name[1:-1])
                            datedict.update({name[1:-1]:date})
                            #print(OKGREEN + name + ENDC)
                            #print(OKGREEN + 'processing ' + name[1:-1] + ENDC)


                else:

                    if lastseen(date) < requirement:
                        late.append(name)
                        names.append(name)
                        latedict.update({name:date})
                        #print(RED + 'processing ' + name + ENDC)

                    else:
                        names.append(name)
                        datedict.update({name:date})
                        #print(OKGREEN + 'processing ' + name + ENDC)

        except AttributeError:
            continue



#for line in late:

#    final = RED + line + ' was last active at: ' + latedict[line] + ENDC
#    print(final)
names.sort()
#print(names)

for line in names:
    if line not in latedict:
        print(OKGREEN + line + OKBLUE + ' was last active at: ' + OKGREEN + datedict[line] + ENDC)
    
    else:
        print(RED + line + OKBLUE + ' was last active at: ' + RED + latedict[line] + ENDC)


