import speech_recognition as sr 
import sys
import os
import datetime
import pyttsx3
from gtts import gTTS
import playsound
import wikipedia
import calendar

# output from computer as voice using gtts lib 

# def say(text):
#     tts=gTTS(text=text,lang='en')
#     fname='temp.mp3'
#     tts.save(fname)
#     playsound.playsound(fname)
# alos use for playing sound
#     os.system('start temp.mp3')

# computer vice using pyttsx3
def  say(text):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id) 
    engine.say(text)
    engine.runAndWait()




#speech recognition
r=sr.Recognizer()
def audio_in():
    with sr.Microphone() as source:
        print("listening")
        audio=r.listen(source)
        text=''

        try:
            text=r.recognize_google(audio).lower()
            print(text)
            
        except Exception as e:
            print("cant able to convert",str(e))
        return text
# for wake word toactivate the assistane
def wakewords(text):
    ww=['hey april','april',' hello april']
    for w in ww:
        if w in text:
            return True

        else: return False
# gives today date
def today_date():
    now=datetime.datetime.now()
    mydate=datetime.datetime.today()
    day=calendar.day_name[mydate.weekday()]
    month=now.month
    daynum=now.day

    month_name=["january",'february',"march",'april','may','june','july','august']

    return "today is {}  {}  {}".format(day,month_name[month-1],daynum)

def greet(text):
    grt=['hi','hellow']

    for word in grt:
        if word in  text:
            return "hellow"

#random.choice(list)
def getperson(text):
    word=text.split()
    if 'who' in word and 'is' in word:
        return ''.join(word[2:])

a=getperson('who is Ms dhoni')
b=wikipedia.summary(a,sentences=4)
say(b)

