from date import datetime
import speech_recognition  as sr   
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#speech engine initialisation

engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice,voices[0].id') #0 -male ,1- female
activationWord ='computer' #single word

#Method to have the system listening for commands

def parsecommand():
    listener = sr.Recognizer()
    print('Listening for  a user command :)') 


