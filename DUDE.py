import pyttsx3
import webbrowser
import random
import requests
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys

engine = pyttsx3.init()


def speak(audio):
    print('DUDE: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello .,DUDE at your service.Please tell me how can I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry .! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()

        if 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")

        else:
            query = query
            speak('Searching...')
            try:

                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak('WIKIPEDIA says - ')
                speak(results)
    
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Please!')
