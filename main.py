from microbit import *
import radio
from functions import *
from images import *
selfID = ''      #No need to change
IDNum = 0
ID = ['Aditya', 'Brishti', 'Corrine', 'Harry', 'Hasini', 'Jaide', 'Kingston', 'Pei', 'Pratham', 'Ron', 'Rupert', 'Smith']
#messages = [Image.HEART, smile, frown, stoneface, owo, waterPistol, arrowup, arrowdown]
#messageNum = 0
#clear button buffers
button_a.was_pressed()
button_b.was_pressed()

# Startup code
while not button_a.was_pressed():
    for i in frames:
        display.show(i)
        sleep(60)
    display.show(frames[-1])
    sleep(200)

#choose your name, and remove it from the list
display.show('WHO ARE YOU?', delay=50)
display.scroll(ID[0], delay=50)
button_b.was_pressed()
selfID = chooseName(ID)
ID.remove(selfID)

display.scroll('CHOOSE YOUR HOMI:', delay=50)
display.scroll(ID[0], delay=50)
#start radio and start main program loop
radio.on()
while True:
    display.show(arrows)
    action = menu(ID, IDNum)
    if action == 'back':
        display.scroll("YOU ARE " + selfID, delay=50)
    elif action == 'confirm':
        display.scroll(ID[IDNum], delay=50)
        #messageNum = chooseMessage(messages)
        #if messageNum == 'back':
        #    continue
        for i in range(1000):
            if accelerometer.is_gesture('shake'):
                sending(ID[IDNum], selfID, Image.HEART)
                break
            sleep(1)
    elif action == 'none':
        pass
    else:
        IDNum = action
        display.scroll(ID[IDNum], delay=50)
    message = radio.receive()
    if message != None:
        message = message.split()
        if message[0] == selfID:
            flashFlash(Image.HEART, 2)
            display.scroll(message[1], delay=50)