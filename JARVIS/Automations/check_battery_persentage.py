import psutil
import os, sys
sys.path.append(os.path.abspath("C:/J.A.R.V.I.S_A.I/JARVIS"))
from Body.Speak.Speak import Speak

def battey_persentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    Speak(f"the device is running on {percent}% battery power")