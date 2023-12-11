from microbit import *
import radio

def flashFlash(image, numTimes):
    def oneFlash(image, time):
        display.show(image)
        sleep(time)
        display.clear()
        sleep(time)
    for i in range(numTimes):
        oneFlash(image, 200)
        oneFlash(image, 200)
        oneFlash(image, 400)

def move(choiceList, choiceNum, direction):
    if direction == 'right':
        if choiceNum == len(choiceList)-1:
            return 0
        else:
            return choiceNum + 1
    if direction == 'left':
        if choiceNum == 0:
            return len(choiceList)-1
        else:
            return choiceNum - 1

def sending(recipient, sender, image):
    radio.send(recipient+" "+sender)
    flashFlash(image, 1)
    flashFlash(Image.ARROW_E, 1)

def buttons_pressed() -> tuple:
    buttons_value = (button_a.was_pressed(), button_b.was_pressed())
    if buttons_value[0]:
        sleep(200)
        buttons_value = (True, button_b.was_pressed())
    elif buttons_value[1]:
        sleep(200)
        buttons_value = (button_a.was_pressed(), True)
    return buttons_value

def menu(options, choiceNum):
    button = buttons_pressed()
    if button[0] and button[1]:
        return 'back'  
    elif button[0]:         #scrolls left
        return move(options, choiceNum, 'left')  
    elif button[1]:           #scrolls right
        return move(options, choiceNum, 'right')
    elif accelerometer.get_x() > 2010:            #starts the sending function and animation
        return 'confirm'
    else: return 'none'

def chooseName(nameList):
    num = 0
    while True:
        action = menu(nameList, num)
        if action == 'back':
            display.scroll("CHOOSE A NAME. SHAKE TO CONFIRM", delay=50)
        elif action == 'confirm':
            display.scroll("YOU ARE " + nameList[num], delay=50)
            return nameList[num]
        elif action == 'none':
            continue
        else:
            num = action
            display.scroll(nameList[num], delay=50)

def chooseMessage(messageList):
    num = 0
    while True:
        action = menu(messageList, num)
        if action == 'back':
            display.scroll('CHOOSE YOUR HOMI:', delay=50)
            return 'back'
        elif action == 'confirm':
            return 'confirm'
        elif action == 'none':
            continue
        else:
            num = action
            display.scroll(messageList[num], delay=50)
