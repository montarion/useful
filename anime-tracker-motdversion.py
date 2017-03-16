import json
import os

import requests


#print("shows that aired recently:\n")
def search():
    #---url for releases, in JSON---#
    url = 'http://www.masterani.me/api/releases'

    #---needed conversion---#
    test = requests.get(url)
    test1 = test.text
    test = str(test1)
    string = json.loads(str(test))
    if os.path.exists('settings.txt'):
        infile = open('settings.txt')
        number = int(infile.readline())
        infile.close()
    else:
        infile = open('settings.txt', 'w')
        number = input('how many shows do you want to see? ')
        infile.write(number)
        print("Written preferred number of shows to 'settings.txt'. You can change your preference there. ")
        infile.close()

    i = 0
    while i < int(number):
        anime = string[i]['anime']['title']
        try:
            print(anime)
        except:
            print("failure to print anime" + i)
        i += 1
search()

