# Standard library imports
import cv2
import os, sys
import pygame

sys.path.append(os.path.abspath("C:/J.A.R.V.I.S_A.I/JARVIS"))
# Local imports

from FUNCTION.Password import Password
from Body.Listen.ListenJs import Listen
from Body.Speak.Speak import Speak
from FUNCTION.Greeting import Greating
from FUNCTION.Jarvis import Respond
from Data.data.DLG import GoodMsg




def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust as needed

def verify_face():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('C:/J.A.R.V.I.S_A.I/JARVIS/FUNCTION/Face_Recognition/trainer/trainer.yml')
    cascadePath = "C:/J.A.R.V.I.S_A.I/JARVIS/FUNCTION/Face_Recognition/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    names = ['', 'Human']  # Modify with your names
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    id = "unknown"  # Initialize id with a default value
    while True:
        ret, img = cam.read()
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])
            if accuracy < 100:
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
        cv2.imshow('camera', img)
        k = cv2.waitKey(10) & 0xff
        if k == 27:  # ESC key to exit
            break
        if id != "unknown":
            break
    cam.release()
    cv2.destroyAllWindows()
    if id == "unknown":
        Speak("Your face is not recognized.")
        return False
    return True




def MainExe():
    os.startfile("C:/J.A.R.V.I.S_A.I/JARVIS/Required/Rainmeter/Rainmeter.exe")
    # Speak("Kindly Provide The Password To Access.")
    # while True:
    #     pas = Listen()  # Get password from user
    #     if Password(pas):  # Check if password is correct
    #         play_sound(r"C:\JARVIS\Data\SoundEffects\open.mp3")
    #         Greating()  # Assuming this function exists
    #         while True:
    #             Respond()  # Assuming this function exists


    if verify_face():
        Speak("Verification have been Successful")
        # Speak("Welcome Back, Haroon Sir!")
        play_sound(r"C:/J.A.R.V.I.S_A.I/JARVIS/Data/SoundEffects/open.mp3")
        Greating()
    while True:
        Respond()
    
# MainExe()