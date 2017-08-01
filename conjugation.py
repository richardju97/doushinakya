# conjugation.py

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
nai = 'ない'
rareru = 'られる'
te = 'て'
you = 'よう'
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
        self.length = len(dic) - 2 #refers to the number of characters in the stem form
        self.computeForms()

    def getStemLength(self):
        return self.length

#    def computeForms(self):
#        res, data = self.accessJisho()

    def computeIchidan(self):
        self.forms['Type'] = 'Ichidan verb'
        
        # Masu Form
        self.forms['Masu'] = (self.forms['Dictionary Form'][:self.length+1] + masu)
        
        # Nai Form
        self.forms['Nai'] = (self.forms['Dictionary Form'][:self.length+1] + nai)

        # Te Form
        self.forms['Te'] = (self.forms['Dictionary Form'][:self.length+1] + te)

        # Potential Form
        self.forms['Potential'] = (self.forms['Dictionary Form'][:self.length+1] + rareru)
    
        # Volitional Form
        self.forms['Volitional'] = (self.forms['Dictionary Form'][:self.length+1] + you)
    
    def computeGodan(self):
        self.forms['Type'] = 'Godan verb'
        
        # Masu Form
        utoi = chr(ord(self.forms['Dictionary Form'][self.length+1])-1)
        self.forms['Masu'] = (self.forms['Dictionary Form'][:self.length+1] + str(utoi) + masu)

        # Nai Form
        if (self.forms['Dictionary Form'][self.length+1] == 'う'):
            utoa = 'わ'
        else:
            utoa = chr(ord(self.forms['Dictionary Form'][self.length+1])-2)
        self.forms['Nai'] = (self.forms['Dictionary Form'][:self.length+1] + str(utoa) + nai)

        # Potential Form
        utoe = chr(ord(self.forms['Dictionary Form'][self.length+1])+1)
        self.forms['Potential'] = (self.forms['Dictionary Form'][self.length+1] + str(utoe) + 'る')

    def computeIrregular(self):
        self.forms['Type'] = 'Irregular verb'

    def computeForms(self):
        r = requests.get(url + self.forms['Dictionary Form']).json()
        status = r['meta']['status']

        if (status == 200):
    #    print("Connection to jisho.org successful")
    
            data = r['data'][0]['senses'][0]
            
            self.forms['English Definition'] = data['english_definitions']
#            print("English Definition: " + str(data['english_definitions']))

#            self.forms['Type of Verb'] = data['parts_of_speech'][0]
#            print("Type of Verb: " + str(data['parts_of_speech']))

    #   If Ru-Verb / Ichidan
            if(data['parts_of_speech'][0] == 'Ichidan verb'):
                self.computeIchidan()
#                print("Masu Form: " + self.forms['Dictionary Form'][:self.length+1] + masu)

    #   If U-Verb / Godan
            elif(data['parts_of_speech'][0][:10] == 'Godan verb'):
                self.computeGodan()
#                print("Masu Form: " + self.forms['Dictionary Form'][:self.length+1] + str(utoi) + masu)
            else:
                self.computeIrregular()

        else:
                print ("Error connecting to jisho.org: " + str(status))
#                return status, None

    def getForms(self):
        return self.forms

    def __str__(self):
        c = "\n"
        for x in self.forms:
            c += (str(x) + ": " + str(self.forms[x]))
            c += '\n'
        
        return c

i = input("Enter Dictionary Form: ")
myWord = doushi(i)
print(myWord)

#stem_length = len(word) - 2
#
#r = requests.get(url + word).json()
#status = r['meta']['status']
#
#if (status == 200):
##    print("Connection to jisho.org successful")
#
#    data = r['data'][0]['senses'][0]
#    print("English Definition: " + str(data['english_definitions']))
#    print("Type of Verb: " + str(data['parts_of_speech']))
#
##   If Ru-Verb
#    if(data['parts_of_speech'][0] == 'Ichidan verb'):
#        print("Masu Form: " + word[:stem_length+1] + masu)
#
##   If U-Verb
#    elif(data['parts_of_speech'][0][:10] == 'Godan verb'):
#        utoi = chr(ord(word[stem_length+1])-1)
#        print("Masu Form: " + word[:stem_length+1] + str(utoi) + masu)
#
#else:
#    print ("Error connecting to jisho.org: " + str(status))
