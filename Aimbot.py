import pyautogui
from time import sleep
import keyboard
from random import randint
import base64
import cv2
import subprocess
var_flag = 0
Sha256 = 'Q3JlYXRlZCBCeTogQ3JhY2tvMjk4'
dat1 = open('_zombie-assets\_clientdat.isz','rb') ; data = dat1.read() ; data1 = base64.b64decode(data) ; data0 = data1.decode('utf-8') ; dat1.close()
dat0 = open('_zombie-assets\_zomdat.isz','rb') ; data12 = dat0.read() ; data10 = base64.b64decode(data12) ; data11 = data10.decode('utf-8') ; dat0.close()
pluginfile = open('_zombie-assets\_airender\_aihack.plg','rb+') ; pluginread = pluginfile.read() ; plugindecrypt = base64.b64decode(pluginread) ; pluginutf8 = plugindecrypt.decode('utf-8') ; pluginfile.close()

if data != Sha256:
    var_flag += 1



print(data0) ; print(" ") ; print(data11) ; print(" ")

subprocess.call([r'_zombie-assets\_airender\_console.bat'])

sleep(1)
keyboard.press_and_release('`')
sleep(0.1)

keyboard.write('stat ai')
keyboard.press_and_release('enter')
sleep(0.1)

keyboard.press_and_release('`')
sleep(0.1)

keyboard.write('show debug')
keyboard.press_and_release('enter')
sleep(3)

if data != 'Q3JlYXRlZCBCeTogQ3JhY2tvMjk4':
    var_flag += 1

while 1==1:

    AI_Rendered0 = pyautogui.locateOnScreen('_zombie-assets\_ren1.png', confidence=0.90) # Image Batch #1
    AI_Rendered1 = pyautogui.locateOnScreen('_zombie-assets\_ren2.png', confidence=0.90)
    AI_Rendered2 = pyautogui.locateOnScreen('_zombie-assets\_ren3.png', confidence=0.90)
    AI_Rendered3 = pyautogui.locateOnScreen('_zombie-assets\_ren4.png', confidence=0.90)
    AI_Rendered4 = pyautogui.locateOnScreen('_zombie-assets\_ren5.png', confidence=0.90)

    if AI_Rendered0 != None:
        print("A Zombie/Oposing AI Has Been Detected.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(AI_Rendered0)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if data != pluginfile:
        var_flag += 1
    
    if AI_Rendered1 != None:
        print("A Zombie/Oposing AI Has Been Detected.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(AI_Rendered1)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if AI_Rendered2 != None:
        print("A Zombie/Oposing AI Has Been Detected.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(AI_Rendered2)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if var_flag >= 4:
        exit()
        
    if AI_Rendered3 != None:
        print("A Zombie/Oposing AI Has Been Detected.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(AI_Rendered3)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue

    if AI_Rendered4 != None:
        print("A Zombie/Oposing AI Has Been Detected.") ; print(" ")
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(AI_Rendered4)
        pyautogui.click(button='left')
        pyautogui.mouseUp(button='right')
        continue
        if var_flag == None: exit()
    sleep(0.2)