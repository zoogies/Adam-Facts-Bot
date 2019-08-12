#imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from groupy.client import Client
import random
import time
import datetime

#variables
discoveries = 0
messagenum1 = 0
messagenum2 = 0
messagenum3 = 0
token = ''
meorhim = 0
skip = 0
i = 0

#functions
def initialize():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('adam-facts-656e16643bf7.json',scope)
    gspreadclient = gspread.authorize(creds)
    sheets = gspreadclient.open('adam_facts').sheet1
    facts = sheets.col_values(2)
    lenlist = len(facts)
    i = 0
    sentbefore = []
    messagenum = 0

def pickmessage(messagenum):
    messagenum = random.randint(0,(lenlist))
    sendmessage(sentbefore,messagenum,discoveries)

def threemessage(messagenum1,messagenum2,messagenum3):
    messagenum1 = random.randint(0,(lenlist))
    messagenum2 = random.randint(0,(lenlist))
    messagenum3 = random.randint(0,(lenlist))

    fakemessage1 = 'Adam Fact #' + str(messagenum1) + ' ' + str(facts[messagenum1])
    fakemessage2 = ', Adam Fact #' + str(messagenum2) + ' ' + str(facts[messagenum2])
    fakemessage3 = ', Adam Fact #' + str(messagenum3) + ' ' + str(facts[messagenum3])
    message = group.post(text=fakemessage1 + fakemessage2 + fakemessage3)

def sendmessage(sentbefore,messagenum,discoveries):
    if len(sentbefore) >= (lenlist):
        sentbefore = []
        pickmessage(messagenum)
    elif messagenum in sentbefore:
        pickmessage(messagenum)
    elif messagenum not in sentbefore:
        discoveries += 1
        factnum = random.randint(0,(lenlist))
        fakemessage = 'Adam Fact #' + str(factnum) + ' ' + str(facts[factnum])
        message = group.post(text=fakemessage)

def animation():
    print('')
    print('Signing In On Token '+token)
    print('')
    time.sleep(1)
    print('(----------)')
    time.sleep(random.randint(1,2))
    print('(#---------)')
    time.sleep(random.randint(1,2))
    print('(##--------)')
    time.sleep(random.randint(1,2))
    print('(###-------)')
    time.sleep(random.randint(1,2))
    print('(####------)')
    time.sleep(random.randint(1,2))
    print('(#####-----)')
    time.sleep(random.randint(1,2))
    print('(######----)')
    time.sleep(random.randint(1,2))
    print('(#######---)')
    time.sleep(random.randint(1,2))
    print('(########--)')
    time.sleep(random.randint(1,2))
    print('(#########-)')
    time.sleep(random.randint(1,2))
    print('(##########)')
    time.sleep(1)

initialize()

#other stuff that i had a hard time putting into a function so i just didnt
print(' ')
print('Welcome To Adam Facts Revision 3.2')
print('')
time.sleep(1)
meorhim = int(input('Adam 1, Me 2: '))
if meorhim == 1:
    #adams
    token = 'lol im not giving you the token just because you looked at the code'
else:
    #mine
    token = 'lol im not giving you the token just because you looked at the code'
print('')
time.sleep(1)
skip = int(input('Enter 0 to skip or 1 to play animation: '))
time.sleep(1)
if skip == 0:
    print('')
    print('Signing In On Token '+token)
    time.sleep(1)
else:
    animation()
print('')
print('Signed in on:')
if token == 'nope you cant find it here either':
    print('Adam Alsko')
else:
    print('Ryan Zmuda')
print('')
time.sleep(1)
client = Client.from_token(token)
groups = list(client.groups.list_all())
print('Listed below are your groups:')
print('')

for group in client.groups.list():
    print(i, '> ', group.name)
    i += 1
    time.sleep(1)
print('')
selectedgroup = int(input('Please enter a group number: '))
group = groups[selectedgroup]
print('')
time.sleep(1)
print('Bot initialized on group '+str(selectedgroup)+'.')
print('')

#While loop for checking recent messages for commands
while True:
        currentDT = datetime.datetime.now()

        messageslist = []
        for message in group.messages.list():
            messageslist.append(message.text)

        if messageslist[0] == '!fact':
            print(str(currentDT) + ' !fact')
            pickmessage(messagenum)
            discoveries = discoveries + 1
            time.sleep(2)

        if messageslist[0] == '!cum':
            print(str(currentDT) + ' !cum')
            group.post('cum')
            time.sleep(2)

        if messageslist[0] == '!discoveries':
            print(str(currentDT) + ' !discoveries')
            group.post('We have discovered ' + str(discoveries) + ' facts out of ' + str(lenlist))
            time.sleep(2)

        if messageslist[0] == '!reset':
            print(str(currentDT) + ' !reset')
            initialize()
            group.post(text='Bot Restarted. ' + str(lenlist) + ' facts loaded.' )

        if messageslist[0] == '!submit':
            print(str(currentDT) + ' !submit')
            group.post('[redacted]')
            time.sleep(2)

        if messageslist[0] == '!list':
            print(str(currentDT) + ' !list')
            group.post('The full list of commands can be found here: [redacted]')
            time.sleep(2)

        if messageslist[0] == '!god':
            print(str(currentDT) + ' !god')
            group.post('god damnit😂')
            time.sleep(2)

        if messageslist[0] == '!recursive':
            print(str(currentDT) + ' !recursive')
            group.post('!recursive')
            time.sleep(1)

        if messageslist[0] == '!fact3':
            print(str(currentDT) + ' !fact3')
            threemessage(messagenum1,messagenum2,messagenum3)
            time.sleep(2)

        if messageslist[0] == '!coinflip':
            coin = random.randint(0,1)
            if coin == 0:
                group.post('Heads!')
                print(str(currentDT) + ' !coinflip heads')
            else:
                group.post('Tails!')
                print(str(currentDT) + ' !coinflip tails')
            time.sleep(2)

        if messageslist[0] == '!adamsay':
            print(str(currentDT) + ' !adamsay called')
            group.post(text='adamsay what?')
            time.sleep(5)
            messageslist = []
            for message in group.messages.list():
                messageslist.append(message.text)
            time.sleep(1)
            if messageslist[0] != '!adamsay':
                group.post(text=messageslist[0])
                print(str(currentDT) + ' !adamsay ' + messageslist[0])
            else:
                group.post(text='something went wrong, were you fast enough?')
                print(str(currentDT) + ' !adamsay error')

        if messageslist[0] == '!how':
            print(str(currentDT) + ' !how')
            group.post('How do you it know this 😂')
            time.sleep(2)

        time.sleep(5)

