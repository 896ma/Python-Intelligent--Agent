from date import datetime
import speech_recognition  as sr   
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#speech engine initialisation

engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice,voices[1].id') #0 -male ,1- female
activationWord ='computer' #single word

def speak(text,rate =120):
    engine.setProperty('rete',rate)
    engine.say(text)
    engine.runAndWait()
    

#Method to have the system listening for commands

def parsecommand():
    listener = sr.Recognizer()
    print('Listening for  a user command :)') 
    
    with sr.Microphone() as source:
        listener.pause_threshold  =2 # how  long can there be a gap in your speech listening before it's cut
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


        
        
        
        
    


