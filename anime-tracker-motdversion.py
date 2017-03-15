import json

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
    anime0 = string[0]['anime']['title']
    anime1 = string[1]['anime']['title']
    anime2 = string[2]['anime']['title']
    anime3 = string[3]['anime']['title']
    anime4 = string[4]['anime']['title']

    try:
        print(anime0)
    except:
        print("failure to get show 1")
        pass
    try:
        print(anime1)
    except:
        print("failure to get show 2")
        pass
    try:
        print(anime2)
    except:
        print("failure to get show 3")
        pass
    try:
        print(anime3)
    except:
        print("failure to get show 4")
        pass
    try:
        print(anime4)
    except:
        print("failure to get show 5")
        pass

search()

