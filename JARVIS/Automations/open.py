import time
import os,sys
import random
import pyautogui as ui
sys.path.append(os.path.abspath("C:/J.A.R.V.I.S_A.I/JARVIS"))
from Data.data.DLG import open_dld
from Body.Speak.Speak import Speak

text = "camera"

def opened(text):
    x = random.choice(open_dld)
    Speak(x+""+text)
    time.sleep(0.5)
    ui.hotkey("win")
    time.sleep(0.2)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")
