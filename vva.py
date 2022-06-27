# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:14:29 2022

@author: josh.smith
"""


import speech_recognition as sr
import datetime
import pocketsphinx
from vosk import Model, KaldiRecognizer
import os


#DONWNLOAD MODEL HERE https://alphacephei.com/vosk/models
# if not os.path.exists('model'):
#     print('u aint got the model')
#     exit(1)

# import pyaudio

# model = Model('model')
# rec = KaldiRecognizer(model,16000)

# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8000)
# stream.start_stream()

# while True:
#     data = stream.read(4000)
#     if len(data) == 0:
#         break
#     if rec.AcceptWaveform(data):
#         print(rec.Result())
#     else: 
#         print(rec.PartialResult())
# print(rec.FinalResult())

# r = sr.Recognizer()
# harvard = sr.AudioFile('Desktop\harvard.wav')
# #there are siz other ones to use all of which require an api
# #but could have more longevity in the future (cap of 50 requests)
# with harvard as source:
#     audio1 = r.record(source,duration=4)
#     audio2 = r.record(source,duration = 4)
# text1 = r.recognize_google(audio1) 
# text2 = r.recognize_google(audio2) 
# print(text1,text2)

# jackhammer = sr.AudioFile('Desktop\jackhammer.wav')
# with jackhammer as source:
#     r.adjust_for_ambient_noise(source,duration = 0.5)
#     audio = r.record(source)
# text3 = r.recognize_google(audio)
# print(text3)

# r = sr.Recognizer()
# #get default mic
# mic= sr.Microphone()

# with mic as source:
#     #get rid of ambient noises
#     r.adjust_for_ambient_noise(source)
#     #use mic to listen
#     audio = r.listen(source)
#use google api to transcipt audio to text
    try:
        #google = r.recognize_google(audio)
        #print(google)
    except:
        print("i didn't recognize that")
    # sphinx = r.recognize_sphinx(audio)
    # print(sphinx)
    #print('Google: [{}]\nSphinx: [{}]\n\n'.format(google,sphinx))
    # print(text)
    #return text as lower instead of making it lower each time
    # if str(text).lower() == 'what time is it':
    #     now = datetime.datetime.now()
    #     print(now.strftime('%I:%M:%S'))
    
    
