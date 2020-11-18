#pip install scrot (only Linux)
import pyautogui as screen
import random as random

screen.FAILSAFE = False;

screen.screenshot("screen.png")

#If we need to find location of an image sub-part on the screen
result = ()
while(True) :
    try :
        result = screen.locateOnScreen("green.png")
        if(len(result) == 4) :
            result = screen.locateCenterOnScreen("green.png")
            screen.moveTo(result,duration=1)
            screen.click()
            print('Found')
    except :
        print('Not found...')
        screen.moveRel(1,1)
    
    try :
        result = screen.locateOnScreen("red2.png")
        if(len(result) == 4) :
            result = screen.locateCenterOnScreen("red2.png")
            screen.moveTo(result,duration=1)
            screen.click()
            print('Found')
    except :
        print('Not found...')
        screen.moveRel(1,1)
    
    try :
        result = screen.locateOnScreen("green2.png")
        if(len(result) == 4) :
            result = screen.locateCenterOnScreen("green2.png")
            screen.moveTo(result,duration=1)
            screen.click()
            print('Found')
    except :
        print('Not found...')
        screen.moveRel(1,1)
    
    print('Waiting...')