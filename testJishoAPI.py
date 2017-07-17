# Python file for testing jisho.org's API

# link to their API, note that their API is also a work in progress
# http://jisho.org/api/v1/search/words?keyword=食べる

url = "http://jisho.org/api/v1/search/words?keyword="

import unicodedata
import json
import requests

word = input("Enter Word to Search: ")

r = requests.get(url + word).json()
status = r['meta']['status']

if (status == 200):
    print("Connection to jisho.org successful")

    data = r['data'][0]['senses']
#    print (data)
    print("English Definition: " + str(data[0]['english_definitions']))
    print("Type of Verb: " + str(data[0]['parts_of_speech']))

else:
    print ("Error connecting to jisho.org: " + str(status))

