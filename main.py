from microbit import *
import radio
arrows = Image('00000:'
               '09090:'
               '90009:'
               '09090:'
               '00000:')

selfID = 'Smith'           #change to own name
IDNo = 0
ID = ['Brishti', 'Hasini', 'Pratham', 'Jaide', 'Harry', 'Corrine', 'Aditya', 'Kingston', 'Rupert', 'Ron', 'Pei', 'Smith']
radio.on()
while True:
    display.show(arrows)
    if button_b.was_pressed():           #scrolls right
      IDNo = IDNo + 1
      display.scroll(ID[IDNo], delay=70)
    elif button_a.was_pressed():         #scrolls left
      IDNo = IDNo - 1
      display.scroll(ID[IDNo], delay=70)
    elif accelerometer.was_gesture('shake'):            #starts the sending function and animation
      display.scroll(ID[IDNo], delay=70)
      radio.send(f"{ID[IDNo]} {selfID}")
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
    message = message.split()
    if message[0] == selfID:
        display.show(Image.HEART)
        sleep(50)
        display.clear()
        sleep(50)
        display.show(Image.HEART)
        sleep(100)
        display.clear()
        sleep(50)
        display.scroll(message[1])