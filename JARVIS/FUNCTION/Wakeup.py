import speech_recognition as sr
import random
import os,sys
sys.path.append(os.path.abspath("C:/J.A.R.V.I.S_A.I/JARVIS"))
from JARVIS.Body.Listen.ListenJs import Listen
from Data.data.DLG import wake_key_word


def Listen(): #listeninig...
    # take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 0.5 #less the number, more it hears
        audio = r.listen(source,0,8) # 0,6 means cut and listen after every 6 SECONDS 
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='eng-in') #for English
        #query = r.recognize_google(audio, language='hi-In') #for Hindi
        print(f'Me:"{str(query)}"\n')
    except Exception as e:
        # print(e) #show full error
        print("Say that again please...")
        return "None"
    return query


def wakeup_command():
    print("Wakeup.py file runing.....")
    #________________________________________________________________________
    sys.path.append(os.path.abspath("C:/JARVIS"))
    from Body.Speak.Speak import Speak
    from MainBuddy.Buddy import MainExe
    #________________________________________________________________________
    Speak('I am sleeping...')

    query = Listen().lower()
    wake_key = random.choice(wake_key_word)
    if wake_key in query:
        print("Entered in query Wakeup.py File")

        #________________________________________________________________________
        sys.path.append(os.path.abspath("C:/JARVIS"))
        from Body.Speak.Speak import Speak
        from MainBuddy.Buddy import MainExe
        #________________________________________________________________________

        Speak("i am Awake")
        #os.startfile(r"C:\JARVIS\Buddy.py")
        MainExe()
    elif 'goodbye' in query:
        Speak("I am shutting down. Good bye Sir!")
        exit()
    else:
        pass


# while True:
#     wakeup_command()
