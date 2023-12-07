from microbit import *
import radio

arrows = Image('00000:'
               '09090:'
               '90009:'
               '09090:'
               '00000:')

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