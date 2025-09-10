import speech_recognition as sr
import sys, os
sys.path.append(os.path.abspath("C:/J.A.R.V.I.S_A.I/JARVIS"))
from Body.Listen.ListenJs import Listen
from Body.Speak.Speak import Speak

def Password(pass_inp):
    password = "1234"
    if pass_inp == password:
        Speak("Access Granted.")
        return True
    else:
        Speak("Access Not Granted. Please provide the correct password.")
        return False

# if __name__ == "__main__" :
#        Speak("Kindly Provide The Password To Access .")
#        pas = Listen()
#        Password(pas)

