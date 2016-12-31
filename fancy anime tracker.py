#things to do!
#let it build urls so users can watch immediately (line 34)
import json
import os
import webbrowser
from time import sleep

import requests


def tracker():
    while True:
        #---url for releases, in JSON---#
        url = 'http://www.masterani.me/api/releases'

        #---needed conversion---#
        test = requests.get(url)
        test1 = test.text
        test = str(test1)
        string = json.loads(str(test))



        #---checks if file containing last aired episode exists. if False, makes it---#
        filecheck = os.path.isfile('lastshow.txt')

        airingshow = string[0]['anime']["title"]
        if filecheck is False:
            lastshow = string[0]['anime']["title"]
            #---writes last aired show to file---#
            infile = open('lastshow.txt', 'w')
            infile.write(lastshow)
            infile.close()
        else:
            #---checks if new show has aired---#
            outfile = open('lastshow.txt')
            check = outfile.read()
            if check != airingshow:
                #---prints actual message---#
                print('alert! ' + string[0]['anime']["title"] + ' episode ' + string[0]["episode"] + ' has aired.')
                #---writes new 'last' show---#
                lastshow = string[0]['anime']["title"]
                infile = open('lastshow.txt', 'w')
                infile.write(lastshow)
                infile.close()

                #---url builder---#
                animeurl = 'http://www.masterani.me/anime/watch/' + string[0]['anime']['slug'] + '/' +string[0]['episode']

                while True:
                    option = input('Do you want to watch now? y/n')
                    if option == 'y':
                        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(animeurl)
                        quit()
                    elif option == 'n':
                        print('Alright, Bye!')
                        quit()
                    else:
                        print('Please reply with either y or n')

            else:
                print('no new shows have aired')
                sleep(300)

tracker()
