# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:14:29 2022

@author: josh.smith
"""


import speech_recognition as sr
import datetime
import pyttsx3
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


WAKE = 'computer'
print('Start')

while True:
    print('Listening')
    text = get_audio()
    if text.count(WAKE) > 0:
        speak('   I am ready')
        text = get_audio()
        if text == 'what time is it':
            now = datetime.datetime.now()
            print(now.strftime('%I:%M:%S'))
        if text == 'stop':
            speak('   exiting')
            break
