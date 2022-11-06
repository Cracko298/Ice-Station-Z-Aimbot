import pyautogui
from time import sleep
import keyboard
from random import randint
import base64
dat1 = open('_zombie-assets\_clientdat.isz','rb') ; data = dat1.read() ; data1 = base64.b64decode(data) ; data0 = data1.decode('utf-8') ; dat1.close()
dat0 = open('_zombie-assets\_zomdat.isz','rb') ; data12 = dat0.read() ; data10 = base64.b64decode(data12) ; data11 = data10.decode('utf-8') ; dat0.close()

print(data0) ; print(" ") ; print(data11) ; print(" ")

while 1==1:

    Zombie0 = pyautogui.locateCenterOnScreen('_zombie-assets\z0.png', confidence=0.65) # Image Batch #1
    Zombie1 = pyautogui.locateCenterOnScreen('_zombie-assets\z1.png', confidence=0.65)
    Zombie2 = pyautogui.locateCenterOnScreen('_zombie-assets\z2.png', confidence=0.65)
    Zombie3 = pyautogui.locateCenterOnScreen('_zombie-assets\z3.png', confidence=0.65)
    Zombie4 = pyautogui.locateCenterOnScreen('_zombie-assets\z4.png', confidence=0.65)
    Zombie5 = pyautogui.locateCenterOnScreen('_zombie-assets\z5.png', confidence=0.65)
    Zombie6 = pyautogui.locateCenterOnScreen('_zombie-assets\z6.png', confidence=0.65)
    Zombie7 = pyautogui.locateCenterOnScreen('_zombie-assets\z7.png', confidence=0.65)
    Zombie8 = pyautogui.locateCenterOnScreen('_zombie-assets\z8.png', confidence=0.65)
    Zombie9 = pyautogui.locateCenterOnScreen('_zombie-assets\z9.png', confidence=0.65)

    Zombie10 = pyautogui.locateCenterOnScreen('_zombie-assets\patch0.png', confidence=0.65) #Image Batch #2
    Zombie11 = pyautogui.locateCenterOnScreen('_zombie-assets\patch1.png', confidence=0.65)

    if Zombie0 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie0)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie1 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie1)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie2 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie2)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie3 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie3)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie4 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie4)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie5 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie5)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie6 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie6)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie7 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie7)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie8 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie8)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie9 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie9)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue


        # Second AI Image Batch Done!

    if Zombie10 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie10)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if Zombie11 != None:
        print("Spotted Zombie.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(Zombie11)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    sleep(0.2)