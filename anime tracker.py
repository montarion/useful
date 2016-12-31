#my first truly own program! made on 12-12-16 made by montarion
# make a function to watch x episode of an anime.
import json
import os
import webbrowser
import winsound
from time import sleep

import requests

print('Welcome to the anime tracker! ')
def updater():
            #---
            #---url for releases, in JSON---#
            url = 'http://www.masterani.me/api/releases'

            #---needed conversion---#
            test = requests.get(url)
            test1 = test.text
            test = str(test1)
            string = json.loads(str(test))
            print('list has been updated')

def search():
    #---url for releases, in JSON---#
    url = 'http://www.masterani.me/api/releases'

    #---needed conversion---#
    test = requests.get(url)
    test1 = test.text
    test = str(test1)
    string = json.loads(str(test))
    anime0 = string[0]['anime']['title']
    anime1 = string[1]['anime']['title']
    anime2 = string[2]['anime']['title']
    anime3 = string[3]['anime']['title']
    anime4 = string[4]['anime']['title']

    searchq = input('what are you looking for? ')
    print('you searched for the term' + ' "' + searchq + '"')
    search0 = searchq.lower() in anime0.lower()
    search1 = searchq.lower() in anime1.lower()
    search2 = searchq.lower() in anime2.lower()
    search3 = searchq.lower() in anime3.lower()
    search4 = searchq.lower() in anime4.lower()


    if searchq == "debug":
        print(anime0)
        print(anime1)
        print(anime2)
        print(anime3)
        print(anime4)
    if search0 == True:
        print(anime0 + ' found! ')
        animeurl = 'http://www.masterani.me/anime/watch/' + string[0]['anime']['slug'] + '/' +string[0]['episode']
        option = input('Do you want to watch it? ')

        if option == 'y' or 'yes':
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(animeurl)
        elif option == 'n':
            print('Alright, bye!')


    elif search1 == True:
        print(anime1 + ' found! ')
        animeurl = 'http://www.masterani.me/anime/watch/' + string[1]['anime']['slug'] + '/' +string[1]['episode']
        option = input('Do you want to watch it? ')

        if option == 'y' or 'yes':
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(animeurl)
        elif option == 'n':
            print('Alright, bye!')



    elif search2 == True:
        print(anime2 + ' found! ')
        animeurl = 'http://www.masterani.me/anime/watch/' + string[2]['anime']['slug'] + '/' +string[2]['episode']
        option = input('Do you want to watch it? ')


        if option == 'y' or 'yes':
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(animeurl)
        elif option == 'n':
            print('Alright, bye!')


    elif search3 == True:
        print(anime3 + ' found! ')
        animeurl = 'http://www.masterani.me/anime/watch/' + string[3]['anime']['slug'] + '/' +string[3]['episode']
        option = input('Do you want to watch it? ')

        if option == 'y' or 'yes':
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(animeurl)
        elif option == 'n':
            print('Alright, bye!')



    elif search4 == True:
        print(anime4 + ' found! ')
        animeurl = 'http://www.masterani.me/anime/watch/' + string[4]['anime']['slug'] + '/' +string[4]['episode']
        option = input('Do you want to watch it? ')

        if option == 'y' or 'yes':
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(animeurl)
        elif option == 'n':
            print('Alright, bye!')
    elif search4 == False:
        print('The term ' + '"' + searchq + '"' + " didn't give any results")


'''def episode():
        episode = input("what episode do you want to watch? \n(Warning! I can't guarrantee that the episode will be available.) ")
        updater()
        episodeurl = 'http://www.masterani.me/anime/watch/' + string[0]['anime']['slug'] + '/' + episode
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(episodeurl)
'''
def alert():

    # Play Windows exit sound.
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)



def loop():

     #---url for releases, in JSON---#
    url = 'http://www.masterani.me/api/releases'

    #---needed conversion---#
    test = requests.get(url)
    test1 = test.text
    test = str(test1)
    string = json.loads(str(test))
    filecheck = os.path.isfile('lastshow.txt')
    airingshow = string[0]['anime']["title"]

    if filecheck is False:
        print("creating file..")
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
            #---prints actual message and plays alert sound---#
            print('alert! ' + string[0]['anime']["title"] + ' episode ' + string[0]["episode"] + ' has aired.')
            alert()
            #---writes new 'last' show---#
            lastshow = string[0]['anime']["title"]
            infile = open('lastshow.txt', 'w')
            infile.write(lastshow)
            infile.close()

            #---url builder---#
            animeurl = 'http://www.masterani.me/anime/watch/' + string[0]['anime']['slug'] + '/' +string[0]['episode']

            while True:
                option = input('Do you want to watch now?')
                if option == 'y' or option == 'yes':
                    while True:
                        episodeoption = input('Do you want to choose your episode or do you want to watch the latest one? ')
                        if episodeoption == 'yes' or episodeoption == 'choose' or episodeoption == 'y':

                            episode = input("what episode do you want to watch? \n(Warning! I can't guarrantee that the episode will be available.) ")

                            episodeurl = 'http://www.masterani.me/anime/watch/' + string[0]['anime']['slug'] + '/' + episode
                            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(episodeurl)

                        elif episodeoption == 'no' or episodeoption == 'latest':
                            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(animeurl)
                        else:
                            print("please reply with either 'yes' or 'choose' if you want to choose your episode, or with 'no' or 'latest' if you want to watch the latest episode")

                    quit()
                if option == 'n' or option == 'no':
                    print("Alright, I'll keep checking. ")
                    loop()
                else:
                    print("Please reply with either 'y 'or ' n'")

        else:
            nonews = "no new shows have aired"
            #print(nonews)
        sleep(6)
        print("looping")
        loop()
def tracker():
    while True:




        #---url for releases, in JSON---#
        url = 'http://www.masterani.me/api/releases'

        #---needed conversion---#
        test = requests.get(url)
        test1 = test.text
        test = str(test1)


        string = json.loads(str(test))

        while True:
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
                menu = input('what do you want to do?')
                if menu == '1' or menu == 'watch':
                    #---checks if new show has aired---#
                    outfile = open('lastshow.txt')
                    check = outfile.read()
                    if check != airingshow:
                        #---prints actual message and plays alert sound---#
                        print('alert! ' + string[0]['anime']["title"] + ' episode ' + string[0]["episode"] + ' has aired.')
                        alert()
                        #---writes new 'last' show---#
                        lastshow = string[0]['anime']["title"]
                        infile = open('lastshow.txt', 'w')
                        infile.write(lastshow)
                        infile.close()

                        #---url builder---#
                        animeurl = 'http://www.masterani.me/anime/watch/' + string[0]['anime']['slug'] + '/' +string[0]['episode']

                        while True:
                            option = input('Do you want to watch now?')
                            if option == 'y' or option == 'yes':
                                while True:
                                    episodeoption = input('Do you want to choose your episode or do you want to watch the latest one? ')
                                    if episodeoption == 'yes' or episodeoption == 'choose' or episodeoption == 'y':

                                        episode = input("what episode do you want to watch? \n(Warning! I can't guarrantee that the episode will be available.) ")

                                        episodeurl = 'http://www.masterani.me/anime/watch/' + string[0]['anime']['slug'] + '/' + episode
                                        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(episodeurl)

                                    elif episodeoption == 'no' or episodeoption == 'latest':
                                        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(animeurl)
                                    else:
                                        print("please reply with either 'yes' or 'choose' if you want to choose your episode, or with 'no' or 'latest' if you want to watch the latest episode")

                                quit()
                            if option == 'n' or option == 'no':
                                print('Alright, Bye!')
                            if option == 'back':
                                tracker()
                            else:
                                print("Please reply with either 'y', 'n', or 'back'")

                    else:
                        #---loop counter---#
                        print('no new shows have aired.')
                        sleep(2)
                if menu == '2' or menu == 'search' or menu == 'find':
                        try:
                            search()
                        except:
                            print("sorry, can't search.")
                        sleep(2)
                if menu == 'help':
                    print("possible commands are: \n'1' to see if a new show has aired. \n'2' to search for the a show. the 5 most recently aired shows are available for search.\n'3' to start standby checking for new shows.\n'4' to exit the program.")
                    sleep(2)
                if menu == '3' or menu == 'loop' or menu == 'standyby':
                    print("starting loop check")
                    loop()
                if menu == '4' or menu == 'exit' or menu == 'quit' or menu == 'leave':
                    print('Alright, goodbye!')
                    quit()

tracker()
