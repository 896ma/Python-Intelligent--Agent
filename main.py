from  datetime import datetime
import speech_recognition  as sr   
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#speech engine initialisation

engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
 #0 -male ,1- female
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

#main loop
if __name__ == '__main__':
    speak('All  systems up and running.')
    
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
                
                
                
                
        
        
    
    
        
        
        
             