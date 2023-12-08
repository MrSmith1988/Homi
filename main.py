from microbit import *
import radio
from functions import *

selfID = 'Smith'  # change to own name
IDNum = 0
ID = ['Aditya', 'Brishti', 'Corrine', 'Harry', 'Hasini', 'Jaide',
      'Kingston', 'Pei', 'Pratham', 'Ron', 'Rupert', 'Smith']

for i in range(len(ID)):
    if selfID == ID[i]:
        display.scroll('Hi '+ID[IDNo], delay=70)
        IDNo = 11
        break
    else:
        IDNo = IDNo+1

radio.on()
while True:
    display.show(arrows)
    button = check_both_buttons()
    if button[0] and button[1]:
        # display user name
        pass

    elif button[0]:  # scrolls left
        IDNum = move(ID, IDNum, 'left')
        display.scroll(ID[IDNum], delay=50)

    elif button[1]:  # scrolls right
        IDNum = move(ID, IDNum, 'right')
        display.scroll(ID[IDNum], delay=50)

    elif accelerometer.get_x() > 2010:  # starts the sending function and animation
        display.scroll(ID[IDNum], delay=50)
        sending(ID[IDNum], selfID, Image.HEART)

    message = radio.receive()
    if message != None:
        message = message.split()
        if message[0] == selfID:
            flashFlash(Image.HEART, 2)
            display.scroll(message[1], delay=50)
