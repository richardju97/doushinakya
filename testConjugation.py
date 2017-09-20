# Test Case File for conjugation.py

# Autocommits when the test case is run
import subprocess
import datetime
n = str(datetime.datetime.now())
subprocess.check_output(['git', 'add', 'conjugation.py', 'testConjugation.py'])
msg = "Commit by Testall on " + n
subprocess.check_output(['git', 'commit', '-m', msg])
subprocess.check_output(['git', 'push', 'origin', 'master'])

# Import conjugation.py
from conjugation import doushi

print("Running all test cases:\n")

def test(num, testa, testb):
    print("====== test" + str(num) + " ======\n")
    print("---- Running test" + str(num) + " ----")

    if(testa == testb):
        print("Test passed.\n")
    else:
        print("Test failed.\n")


#Test 1:
#Ichidan Verbs
#食べる　食べます　食べよう　食べない　食べて　食べられる　to eat
test1 = doushi("食べる").getForms()
test1sol = {'Dictionary Form': '食べる',
            'English Definition': ['to eat'],
            'Type': 'Ichidan verb',
            'Masu': '食べます',
            'Nai': '食べない',
            'Te': '食べて',
            'Potential': '食べられる',
            'Volitional': '食べよう'
}

test(1, test1, test1sol)

#Test 2:
#Godan Verbs w/　う

test2 = doushi("言う").getForms()
test(2, test2, test1sol)

#Test 3:
#Godan Verbs w/　く
#
#Test 4:
#Godan Verbs w/ ぐ
#
#Test 5:
#Godan Verbs w/　す

test5 = doushi("話す").getForms()
test5sol = {'Dictionary Form': '話す',
            'English Definition': ['to talk', 'to speak', 'to converse', 'to chat'],
            'Type': 'Godan verb',
            'Masu': '話します',
            'Nai': '話さない',
            'Te':'話して',
            'Potential':'話せる',
            'Volitional':'話そう'
}
test(5, test5, test5sol)

#Test 6:
#Godan Verbs w/ ず
#
#Test 7:
#Godan Verbs w/　つ
#
#Test 8:
#Godan Verbs / づ
#
#Test 9:
#Godan Verbs w/ ぬ
#
#Test 10:
#Godan Verbs w/ ふ
#
#Test 11:
#Godan Verbs w/ ぶ
#
#Test 12:
#Godan Verbs w/ ぷ
#
#Test 13:
#Godan Verbs w/ む
#飲む　飲みます　飲もう　飲まない　飲んで　飲める　to drink
#
#Test 14:
#Godan Verbs w/ る
#成る　成ります　成ろう　成らない　（）　成れる　to become
#
#Test 15:
#Godan Verbs w/ ゆ
#
#Test 16:
#Irregular Verb -　する
#する　します　しよう　しない　（）　でくる　to do
#
#Test 17:
#Irregular Verb - 来る
#来る　来ます　（）　来ない　（）　（）　to come

#What happens to suru verbs? E.g. 散歩する
