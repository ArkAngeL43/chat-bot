import os 
import time
import sys 
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

#define the bot
bot = ChatBot('Buddy')

# connection to database 
bot = ChatBot(
    'Buddy', #buddy is bots name 
    storage_adapter='chatterbot.storage.SQLStorageAdapter', 
    database_uri='sqlite:///database.sqlite3' #DB STORAGE 
)
#logical adapting connection 
bot = ChatBot(
    'Buddy',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)
os.system(' clear ')
os.system(' cls ')
trainer = ListTrainer(bot)

# if hi is said bot will go down line in trainer 
# and will output hello but 
# if line is said like with? AI will reply with time? but there is no time in the code

# conclusion? how and why would it output the time?

trainer.train([ # this is the training script for the bot 
'Hi',
'hello there',
'i need help',
'what do you need help with',
'i need to scan a network area',
'try sudo airodump-ng and your wireless interface',
])

trainer.train([
'hi',
'why hello there',
'what can you do?',
'well i can do nothing',
'ok then bye',
'bye',


])

os.system(' clear ')

#get the response of the user 
#response = bot.get_response('i need to launch an attack')

#bot response
#print("Bot Response:", response)

name=input("Enter Your Name: ") # name input  
print( "Welcome to the Bot Service! Let me know how can I help you " + name )
os.system(' clear ')
while True:
    request=input(name+':') 
    if request=='Bye' or request =='bye':
        time.sleep(1)
        print('AI Mark => have a nice one! goodBye') # prints bye message 
        break # breaks 
    if request=='hell' or request =='HELL':
        time.sleep(1)
        print('AI Mark => what the fuck ')
        break
    else:
        response=bot.get_response(request)
        print('AI Mark => ',response) # if else happens print the response 



########## DEV NOTES #######


# first test 

#Enter Your Name: Death 
#Welcome to the Bot Service! Let me know how can I help you?
#Death :hello
#Bot: I need your assistance
#Death :with?
#Bot: The current time is 10:21 AM
#Death :hi
#Bot: hello


# anything starting with wh like why, when, who, where will say the time. why?