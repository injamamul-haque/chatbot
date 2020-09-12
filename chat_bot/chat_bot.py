from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
'''
import pyttsx3
import engineio


engineio = pyttsx3.init('espeak')
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 150)    # Aquí puedes seleccionar la velocidad de la voz
engineio.setProperty('voice',voices[-3].id)'''

'''def speak(text):
    engineio.say(text)
    engineio.runAndWait()'''



bot=ChatBot('Bot')
trainer=ListTrainer(bot)
"""print("choose your language")
print("1----> english\n2---->bengali\n3---->thai\n4---->hindi\n5---->italian\n6---->japanese\n7---->korean\n8---->telugu\n9---->french\n10---->german\n11---->hebrew\n12---->indonesian\n13---->marathi\n14---->oriya\n15---->persian\n16---->portuguese\n17---->russian\n18---->spanish\n19---->swedish\n20---->traditionalchinese\n21---->for exit type bye")"""
#lag=input()
#if(lag=="english"):
       for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files,'r').readlines()
             trainer.train(data)
"""elif(lag=="bengali"):
       for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/bengali/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/bengali/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="thai"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/thai/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/thai/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="hindi"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/hindi/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/hindi/' + files,'r').readlines()
             trainer.train(data) 
elif(lag=="italian"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/italian/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/italian/' + files,'r').readlines()
             trainer.train(data) 
elif(lag=="japanese"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/japanese/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/japanese/' + files,'r').readlines()
             trainer.train(data) 
elif(lag=="korean"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/korean/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/korean/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="telugu"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/telugu/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/telugu/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="french"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/french/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/french/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="german"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/german/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/german/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="hebrew"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/hebrew/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/hebrew/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="indonesian"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/indonesian/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/indonesian/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="marathi"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/marathi/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/marathi/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="oriya"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/oriya/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/oriya/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="persian"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/persian/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/persian/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="portuguese"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/portuguese/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/portuguese/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="russian"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/russian/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/russian/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="spanish"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/spanish/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/spanish/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="swedish"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/swedish/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/swedish/' + files,'r').readlines()
             trainer.train(data)
elif(lag=="traditionalchinese"):
        for files in os.listdir('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/traditionalchinese/'):
             data= open('/home/injamamul/Desktop/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/traditionalchinese/' + files,'r').readlines()
             trainer.train(data)
#print("enter your name")
#name=input() """
while True:
   message=input("injamamul :")
   if message.strip()!='bye':
      reply = bot.get_response(message)
      #print(chatbot,reply)
      print('chatbot :',reply)
     # speak(reply)
     # print(voices)
   if message.strip()=='bye':
       #print(chatbot,"bye")
      print('chatbot : bye')
      # speak('bye')
      break


