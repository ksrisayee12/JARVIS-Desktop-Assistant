# Importing Packages
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser

# Creating Listener And Engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Creating A Speaking Engine
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Creating A Speech Recognizer
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass    
    return command

# Welcome Speech Method
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('good morning')
    elif hour >= 12 and hour < 18:
        talk('good afternoon')
    else:
        talk('good evening')
    talk('i am jarvis your personal A  I assistant')
    talk('how can i help you')

# Main JARVIS Method
def run_jarvis():
    command = take_command()
    print(command)
    # For Playing Songs On YouTube 
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    # For Telling Time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is' + time)

    # Searching Queries On Wikipedia
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 6)
        print('According to wikipedia')
        print(info)
        talk('according to wikipedia')
        talk(info) 

    # Time For A Joke
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    # Just Fun Commands
    elif 'how are you' in command:
        print('i am alright how are you sir')
        talk('i am alright how are you sir')

    elif 'i am fine' in command:
        print('ok how can i help you')
        talk('ok how can i help you')

    # Searching Queries On Google
    elif 'search' in command:
        result = command.replace('search', '')
        talk('searching ' + result + 'on google')
        pywhatkit.search(result)

    # Opening Apps
    elif 'open vs code' in command:
        codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        talk('opening visual studio code')
        os.startfile(codePath)

    elif 'open notepad' in command:
        notepadPath = "C:\\WINDOWS\\system32\\notepad.exe"
        talk('opening notepad')
        os.startfile(notepadPath)

    elif 'open chrome' in command:
        chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        talk('opening chormme')
        os.startfile(chromePath)

    elif 'open microsoft browser' in command:
        edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        talk('opening edge browser')
        os.startfile(edgePath)

    elif 'open firefox' in command:
        firefoxPath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
        talk('opening firefox')
        os.startfile(firefoxPath)

    elif 'open command prompt' in command:
        cmdPath = "C:\\WINDOWS\\system32\\cmd.exe"
        talk('opening command prompt')
        os.startfile(cmdPath)

    elif 'open python editor' in command:
        pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"
        talk('opening py charm')
        os.startfile(pycharmPath)

    elif 'open obs studio' in command:
        obsPath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
        talk('opening obs studio')
        os.startfile(obsPath)

    elif 'open python browser' in command:
        pythonBrowserPath = "D:\\Srisayee K\\Coding\\A.I PROJECTS\\Speech-Recognition-Projects\\Jarvis-Desktop-Assistant\\Browser.py"
        talk('opening Python Browser')
        os.startfile(pythonBrowserPath)

    # Opening Websites
    elif 'open youtube' in command:
        talk('opening youtube')
        webbrowser.open('www.youtube.com')

    elif 'open google' in command:
        talk('opening google')
        webbrowser.open('www.google.com')

    elif 'open stackoverflow' in command:
        talk('opening stackoverflow')
        webbrowser.open('www.stackoverflow.com')

    elif 'open facebook' in command:
        talk('opening facebook')
        webbrowser.open('www.facebook.com')

    elif 'open instagram' in command:
        talk('opening instagram')
        webbrowser.open('www.instagram.com')

    elif 'open github' in command:
        talk('opening github')
        webbrowser.open('www.github.com')

    elif 'open spotify' in command:
        talk('opening spotify')
        webbrowser.open('www.spotify.com')
        
    elif 'open linkedin' in command:
        talk('opening linkedin')
        webbrowser.open('www.linkedin.com')
        
    elif 'open whatsapp' in command:
        talk('opening whatsapp web')
        webbrowser.open('https://web.whatsapp.com/')

    elif 'open maps' in command:
        talk('opening google maps')
        webbrowser.open('https://www.google.com/maps')

    elif 'open g drive' in command:
        talk('opening google drive')
        webbrowser.open('https://drive.google.com/')

    elif 'open g documents' in command:
        talk('opening google docs')
        webbrowser.open('https://docs.google.com/')

    elif 'open g meet' in command:
        talk('opening google meet')
        webbrowser.open('https://meet.google.com/')

    elif 'open amazon' in command:
        talk('opening amazon')
        webbrowser.open('https://www.amazon.com/')

    elif 'open flipkart' in command:
        talk('opening flipcart')
        webbrowser.open('https://www.flipkart.com/')

    elif 'open netflix' in command:
        talk('opening netflix')
        webbrowser.open('https://www.netflix.com/')

    elif 'open brainly' in command:
        talk('opening brainly')
        webbrowser.open('https://brainly.com/')

    elif 'open byjus' in command:
        talk('opening byjus')
        webbrowser.open('https://byjus.com/')

    # About Jarvis And The Creator
    elif 'who is your creator' in command:
        talk('I was created by sri saayii')
        print('I was created by sri sayee')

    elif 'who created you' in command:
        talk('I was created by sri   saayii')
        print('I was created by sri sayee')

    elif 'introduce yourself' in command:
        print('i am jarvis your personal A  I assistant i was created by sri sayee i am a advanced version of AI alexa created by sri sayee')        
        talk('i   am   jarvis   your   personal   A   I   assistant   i   was   created   by   sri   saayii   i   am   a   advanced   version   of   A  I   alexa   created   by   sri   saayii')        
        print('i can open apps open youtube videos tell jokes tell time searches your query on wikipedia and google')
        talk('i   can   open   apps   open   youtube   videos   tell   jokes   tell   time   searches    your    query    on   wikipedia   and   google')

    # Checking if any error in the command and asking for repeating
    else:
         talk('Please say that command again')

# Running Wishme function
if __name__ == '__main__':
    print('i am jarvis your personal AI assistant')
    wishme()
    print('how can i help you')

# Running Jarvis function
while True:
    run_jarvis()

    commandLine = take_command()

    # Giving JARVIS a exit command
    if 'exit' in commandLine:
        talk('ok sir let me exit')
        break