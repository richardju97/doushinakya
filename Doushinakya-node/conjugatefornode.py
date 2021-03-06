# conjugatefornood.py
# conjugation.py modified to be called by and return the result to the nodejs app

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
masu = "ます"
nai = "ない"
rareru = "られる"
te = "て"
you = "よう"
#
# # Ru-Verbs
# # print masuForm[:stem_length+1] + masu.decode("utf-8")
# 
# # U-Verbs
# # utoe = unichr(ord(masuForm[stem_length+1])-1)
# # print "Masu Form: " + masuForm[:stem_length+1] + utoe + masu.decode("utf-8")
# 
# # Irregular Verbs
# if (masuForm == ("いく").decode("utf-8")):
# 	masuForm = ("行き").decode("utf-8")
# 	print masuForm + masu.decode("utf-8")
# elif (masuForm == ("くる").decode("utf-8")):
# 	masuForm = ("来").decode("utf-8")
# 	print masuForm + masu.decode("utf-8")
# else:
# 	print "Verb is neither"
# 	
# # print masuForm + masu.decode("utf-8")
# 
# 
# # Other forms still needed: Volitional, Te-Form, Ta-Form?, Negative, Potential

# Either functions with dic -> masu, masu -> dic, etc. or object initialized with dictionary form

kuruForms = {"Dictionary Form": "来る",
            "English Definition": ["to come (spatially or temporally)", "to approach", "to arrive"],
            "Type": "Irregular verb",
            "Masu": "来ます",
            "Nai": "来ない",
            "Te":"来て",
            "Potential":"来られる",
            "Volitional":"来よう"
}

suruBase = {"Dictionary Form": "する",
            "English Definition": ["to do"],
            "Type": "Irregular verb",
            "Masu": "します",
            "Nai": "しない",
            "Te":"して",
            "Potential":"できる",
            "Volitional":"しよう"
}

class doushi:
    def __init__(self, dic):
        self.forms = {"Dictionary Form" : dic}
        self.length = len(dic) - 2 #refers to the number of characters in the stem form
        self.computeForms()

    def getStemLength(self):
        return self.length

#    def computeForms(self):
#        res, data = self.accessJisho()

    def computeIchidan(self):
        self.forms["Type"] = "Ichidan verb"
        
        stem = self.forms["Dictionary Form"][:self.length+1]
        
        # Masu Form
        self.forms["Masu"] = (stem + masu)
        
        # Nai Form
        self.forms["Nai"] = (stem + nai)

        # Te Form
        self.forms["Te"] = (stem + te)

        # Potential Form
        self.forms["Potential"] = (stem + rareru)
    
        # Volitional Form
        self.forms["Volitional"] = (stem + you)
    
    def computeGodan(self):
        self.forms["Type"] = "Godan verb"
        stem = self.forms["Dictionary Form"][:self.length+1]

        # Masu Form
        last = self.forms["Dictionary Form"][self.length+1]
        utoi = None
        if (last <= "ぞ"):
            utoi = chr(ord(last)-2)
        elif (last == "る" or last == "む" or last == "ぬ"):
            utoi = chr(ord(last)-1)
        elif (last <= "ぽ"):
            utoi = chr(ord(last)-3)
#        else:
#            utoi = chr(ord(last)-3)

        self.forms["Masu"] = (self.forms["Dictionary Form"][:self.length+1] + str(utoi) + masu)

        # Nai Form
        if (last == "う"):
            utoa = "わ"
        elif (last <= "ぞ"):
            utoa = chr(ord(last)-4)
        elif (last == "る" or last == "む" or last == "ぬ"):
            utoa = chr(ord(last)-2)
        elif (last <= "づ"):
            utoa = chr(ord(last)-5)
        elif (last <= "ぽ"):
            utoa = chr(ord(last)-6)


        self.forms["Nai"] = (self.forms["Dictionary Form"][:self.length+1] + str(utoa) + nai)

        # Te Form
        # u tsu ru -> small tsu te
        # ku -> i te, gu -> i de
        # nu bu mu -> nde
        # su -> shite
        # iku -> itte
        
        sound = self.forms["Dictionary Form"][self.length+1]
        
        if (self.forms["Dictionary Form"] == "行く"):
            self.forms["Te"] = "行って"
        elif(sound == "す"):
            self.forms["Te"] = stem + "して"
        elif(sound == "ぬ" or sound == "ぶ" or sound == "む"):
            self.forms["Te"] = stem + "んで"
        elif(sound == "う" or sound == "つ" or sound == "る"):
            self.forms["Te"] = stem + "って"
        elif(sound == "く"):
            self.forms["Te"] = stem + "いて"
        elif(sound == "ぐ"):
            self.forms["Te"] = stem + "いで"
        else:
            self.forms["Te"] = "ERROR"

        # Potential Form
        if (last <= "づ"):
            utoe = chr(ord(last)+2)
        elif (last == "る" or last == "む" or last == "ぬ"):
            utoe = chr(ord(last)+1)
        elif (last <= "ぽ"):
            utoa = chr(ord(last)+3)
        self.forms["Potential"] = (stem + str(utoe) + "る")
            
        # Volitional Form
        u = "う"

        if (last <= "づ"):
            utoo = chr(ord(last)+4)
        elif (last == "る" or last == "む" or last == "ぬ"):
            utoo = chr(ord(last)+2)
        elif (last <= "ぽ"):
            utoo = chr(ord(last)+6)

#        utoo = chr(ord(self.forms["Dictionary Form"][self.length+1]) + 4)
        self.forms["Volitional"] = (stem + utoo + u)

    def computeIrregular(self):
        if (self.forms["Dictionary Form"] == "来る"):
            self.forms = kuruForms
        elif(self.forms["Dictionary Form"] == "する"):
            self.forms = suruBase
        else:
            stem = self.forms["Dictionary Form"][:self.length]
            self.forms["Type"] = "Irregular verb"
            self.forms["Masu"] = stem + suruBase["Masu"]
            self.forms["Nai"] = stem + suruBase["Nai"]
            self.forms["Te"] = stem + suruBase["Te"]
            self.forms["Potential"] = stem + suruBase["Potential"]
            self.forms["Volitional"] = stem + suruBase["Volitional"]

    def computeForms(self):
        r = requests.get(url + self.forms["Dictionary Form"]).json()
        status = r["meta"]["status"]

        if (status == 200):
    #    print("Connection to jisho.org successful")
    
            data = r["data"][0]["senses"][0]
            self.forms["English Definition"] = data["english_definitions"]

    #   If Ru-Verb / Ichidan
            if(data["parts_of_speech"][0] == "Ichidan verb"):
                self.computeIchidan()

    #   If U-Verb / Godan
            elif(data["parts_of_speech"][0][:10] == "Godan verb"):
                self.computeGodan()
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
            c += "\n"
        
        return c

#i = input("Enter Dictionary Form: ")
#myWord = doushi(i)
#print(myWord)

#stem_length = len(word) - 2
#
#r = requests.get(url + word).json()
#status = r["meta"]["status"]
#
#if (status == 200):
##    print("Connection to jisho.org successful")
#
#    data = r["data"][0]["senses"][0]
#    print("English Definition: " + str(data["english_definitions"]))
#    print("Type of Verb: " + str(data["parts_of_speech"]))
#
##   If Ru-Verb
#    if(data["parts_of_speech"][0] == "Ichidan verb"):
#        print("Masu Form: " + word[:stem_length+1] + masu)
#
##   If U-Verb
#    elif(data["parts_of_speech"][0][:10] == "Godan verb"):
#        utoi = chr(ord(word[stem_length+1])-1)
#        print("Masu Form: " + word[:stem_length+1] + str(utoi) + masu)
#
#else:
#    print ("Error connecting to jisho.org: " + str(status))

ret = doushi(sys.argv[1]).getForms()
print(ret)
sys.stdout.flush()
