import json

import requests
print("shows that aired recently:\n")
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

    print(anime0)
    print(anime1)
    print(anime2)
    print(anime3)
    print(anime4)
search()
