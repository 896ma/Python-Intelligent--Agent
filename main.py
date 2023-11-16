from  datetime import datetime
import speech_recognition  as sr   
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import math
import  time
#speech engine initialisation

engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
 #0 -male ,1- female
activationWord ='Patek' #single word

#Browser configuration
#set the path for the web browser 


# Mute ALSA errors...
from ctypes import *
from contextlib import contextmanager

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    try: 
        asound = cdll.LoadLibrary('libasound.so')
        asound.snd_lib_error_set_handler(c_error_handler)
        yield
        asound.snd_lib_error_set_handler(None)
    except:
        yield
        print('')
chrome_path = "/usr/bin/google-chrome"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))



def search_wikipedia(keyword=''):
    searchResults = wikipedia.search(keyword)
    if not searchResults:
        return 'No result received'
    try: 
        wikiPage = wikipedia.page(searchResults[0]) 
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

def speak(text,rate =190):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()
    

#Method to have the system listening for commands

def parsecommand():
    listener = sr.Recognizer()
    print('Listening for  a user command :)') 
    
    with sr.Microphone() as source:
        listener.pause_threshold  =5 # how  long can there be a gap in your speech listening before it's cut
        input_speech =listener.listen(source)
        
        
    try:
        print('Recognizing Speech...')
        query =listener.recognize_google(input_speech,language='en_US')
        print(f'The input speech was:(query)')#How well was the speech recognized
    except Exception as exception:
        print('Sorry but I did not quite catch that :)')
        speak('Sorry but I did not quite catch that')
        print(exception)
        return 'None'
    return query

#main loop
if __name__ == '__main__':
    speak('All  systems up and  running .')
    
    while True:
        #parse  arguments as a list( store whatever user says as a list of different words)
        query =parsecommand().lower().split()
        if query[0] == activationWord:
            query.pop(0)
        
        #list commands
        if  query[0] == 'say':
            if 'hello' in query:
                speak('Greetings , Solar Crash')
                
            else:
                query.pop(0) #  Remove the  say command again from your list
                speech =''.join(query)
                speak(speech) #  Echo from your  AI assistant 
                
                #Navigation
                
            if query[0]== 'go' and query[1]== 'to':
                speak('opening...')
                query = ''.join(query[2:])
                webbrowser.get('chrome').open_new(query)
                
             # Wikipedia
            if query[0] == 'wikipedia':
                query = ' '.join(query[1:])
                speak('Querying the universal databank')
                time.sleep(2)
                speak(search_wikipedia(query))
        
        
    
    
        
        
        
             