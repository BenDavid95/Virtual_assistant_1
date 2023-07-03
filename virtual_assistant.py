import speech_recognition as sr
import pyttsx3 #txt to speech
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
listener.energy_threshold = 4000
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command1 = listener.recognize_google(voice)
            
    except:
        command1=None
        pass
    return command1
    
        
    


def run_tommy():
    
    command = take_command()
    print(command)
    if command==None:
        talk('Please say the command again.')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'thank you goodbye' in command:
        talk("bye bye see you soon")
        exit()
    
    
        
        


while True:
    run_tommy()
