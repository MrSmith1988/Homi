from microbit import *
import radio
arrows = Image('00000:'
               '09090:'
               '90009:'
               '09090:'
               '00000:')

selfID = 'Brishti'           #change to own name
IDNo = 0
ID = ['Aditya', 'Brishti', 'Corrine', 'Harry', 'Hasini', 'Jaide', 'Kingston', 'Pei', 'Pratham', 'Ron', 'Rupert', 'Smith']
radio.on()
while True:
    display.show(arrows)
    if button_b.was_pressed():           #scrolls right
        if IDNo == len(ID)-1:
            IDNo = 0
        else:
            IDNo = IDNo + 1
        display.scroll(ID[IDNo], delay=50)
    elif button_a.was_pressed():         #scrolls left
        if IDNo == 0:
            IDNo = len(ID)-1
        else:
            IDNo = IDNo - 1
        display.scroll(ID[IDNo], delay=50)
    elif accelerometer.was_gesture('shake'):            #starts the sending function and animation
        display.scroll(ID[IDNo], delay=50)
        radio.send(ID[IDNo]+" "+selfID)
        display.show(Image.HEART)
        sleep(500)
        display.show(Image.ARROW_E)
        sleep(500)
        display.clear()
        sleep(250)
        display.show(Image.ARROW_E)
        sleep(500)
        display.clear()
        sleep(250)
        display.show(Image.ARROW_E)
        sleep(500)
        display.clear()

    message = radio.receive()
    if message != None:
        message = message.split()
        if message[0] == selfID:
            display.show(Image.HEART)
            sleep(200)
            display.clear()
            sleep(200)
            display.show(Image.HEART)
            sleep(200)
            display.clear()
            sleep(200)
            display.show(Image.HEART)
            sleep(400)
            display.clear()
            sleep(200)
            display.scroll(message[1], delay=50)