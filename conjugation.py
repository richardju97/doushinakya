# Conjugation.py

import unicodedata
import sys
import json
import requests

url = "http://jisho.org/api/v1/search/words?keyword="

# Functions Needed
# Dictionary -> Masu
# Masu -> Dictionary

# Not sure if I need these two
# Masu -> Mashita (Past Tense)
# Mashita -> Masu


# Copied over from testJapanese.py in python-scripts REPO
# dictionaryForm = raw_input("Dictionary Form: ")
# # print "Dictionary Form: " + dictionaryForm
# 
# masuForm = dictionaryForm.decode("utf-8")
# stem_length = len(masuForm) - 2
# 
masu = 'ます'
#
# # Ru-Verbs
# # print masuForm[:stem_length+1] + masu.decode("utf-8")
# 
# # U-Verbs
# # utoe = unichr(ord(masuForm[stem_length+1])-1)
# # print "Masu Form: " + masuForm[:stem_length+1] + utoe + masu.decode("utf-8")
# 
# # Irregular Verbs
# if (masuForm == ('いく').decode("utf-8")):
# 	masuForm = ('行き').decode("utf-8")
# 	print masuForm + masu.decode("utf-8")
# elif (masuForm == ('くる').decode("utf-8")):
# 	masuForm = ('来').decode("utf-8")
# 	print masuForm + masu.decode("utf-8")
# else:
# 	print "Verb is neither"
# 	
# # print masuForm + masu.decode("utf-8")
# 
# 
# # Other forms still needed: Volitional, Te-Form, Ta-Form?, Negative, Potential

# Either functions with dic -> masu, masu -> dic, etc. or object initialized with dictionary form

class doushi:
    def __init__(self, dic):
        self.forms = {'Dictionary Form' : dic}
        self.stem_length = len(dic) - 2

i = input("Enter Dictionary Form: ")
stem_length = len(word) - 2

r = requests.get(url + word).json()
status = r['meta']['status']

if (status == 200):
#    print("Connection to jisho.org successful")

    data = r['data'][0]['senses'][0]
    print("English Definition: " + str(data['english_definitions']))
    print("Type of Verb: " + str(data['parts_of_speech']))

#   If Ru-Verb
    if(data['parts_of_speech'][0] == 'Ichidan verb'):
        print("Masu Form: " + word[:stem_length+1] + masu)

#   If U-Verb
    elif(data['parts_of_speech'][0][:10] == 'Godan verb'):
        utoi = chr(ord(word[stem_length+1])-1)
        print("Masu Form: " + word[:stem_length+1] + str(utoi) + masu)

else:
    print ("Error connecting to jisho.org: " + str(status))
