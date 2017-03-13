import socket
import wget
import os

if os.path.exists('tld.txt'):
    pass
else:
    wget.download('https://raw.githubusercontent.com/incognico/list-of-top-level-domains/master/tlds.csv', 'tld.txt')

infile = open('tld.txt', encoding='UTF-8')



tlist = []
flist = []
i = 0
x = 0
#add percentage counter using x here..
while i < 285:
    data = infile.readline()
    ugh = data.split(',')
    tlist.append(ugh)

    var = tlist[i][0]
    var = '.' + var

    flist.append(var)

    #print(flist)
    i += 1
    x += 1

infile.close()

#actual checking

url = input('well? ')
print('please wait..')
i = 0
error = '***'


failure = []
succes = []
while i < 285:

    host = url + flist[i]
    try:
        result = socket.gethostbyname(host)
        print(host + " has ip: " + result)
        succes.append(host)
    except:
        print("looking up: " + host + ' resulted in failure')
        failure.append(host)
    i += 1
    x += 1
print("these are taken: " + str(succes))

