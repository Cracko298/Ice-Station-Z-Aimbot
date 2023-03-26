import pyautogui
import pydirectinput
from time import sleep
from os import remove
from os import path
import keyboard
from os import path
import cv2 

number = 1


check_win = path.exists("C:\Windows\SysWOW64") # Linux, MacOS, or Windows Detection
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'


while number == 1:

    afk0 = pyautogui.locateCenterOnScreen('patch.png', confidence=0.90)
    afk1 = pyautogui.locateCenterOnScreen('patch0.png', confidence=0.95)
    afk2 = pyautogui.locateCenterOnScreen('patch1.png', confidence=0.95)
    afk3 = pyautogui.locateCenterOnScreen('patch2.png', confidence=0.97)
    afk4 = pyautogui.locateCenterOnScreen('patch3.png', confidence=0.90)
    afk5 = pyautogui.locateCenterOnScreen('patch4.png', confidence=0.90)
    afk6 = pyautogui.locateCenterOnScreen('patch5.png', confidence=0.95)
    afk7 = pyautogui.locateCenterOnScreen('patch6.png', confidence=0.75)
    afk8 = pyautogui.locateCenterOnScreen('patch7.png', confidence=0.75)

    if keyboard.is_pressed('Alt'):
        break

    if afk0 != None:
        pyautogui.moveTo(afk0)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x,y)
        pydirectinput.click()
    
    if afk1 != None:
        pyautogui.moveTo(afk1)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x,y)
        pydirectinput.click()

    if afk2 != None:
        pyautogui.moveTo(afk2)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x,y)
        pydirectinput.click()

    if afk3 != None:
        pyautogui.moveTo(afk3)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x,y)
        pydirectinput.click()

    if afk4 != None:
        pyautogui.moveTo(afk4)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x,y)
        pydirectinput.click()

    if afk5 != None:
        pyautogui.moveTo(afk5)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x,y)
        pydirectinput.click()

    if afk6 != None:
        pyautogui.moveTo(afk6)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x,y)
        pydirectinput.click()

    if afk7 != None:
        pyautogui.moveTo(afk7)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x+5,y)
        pydirectinput.click()

    if afk8 != None:
        pyautogui.moveTo(afk8)
        x,y = pyautogui.position()
        pydirectinput.moveRel(x+5,y)
        pydirectinput.click()


