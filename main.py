from microbit import *
import radio
arrows = Image('00000:'
               '09090:'
               '90009:'
               '09090:'
               '00000:')

selfID = 'Hasini'           #change to own name
IDNo = 0
ID = ['Brishti', 'Hasini', 'Pratham', 'Jaide', 'Harry', 'Corrine', 'Aditya', 'Kingston', 'Rupert', 'Ron', 'Pei']
radio.on()
while True:
  display.show(arrows)
  for n in ID:
    if button_b.is_pressed():           #scrolls right
      IDNo = IDNo + 1
      display.scroll(ID[IDNo])
    elif button_a.is_pressed():         #scrolls left
      IDNo = IDNo - 1
      display.scroll(ID[IDNo])
    elif accelerometer.was_gesture('shake'):            #starts the sending function and animation
      display.scroll(ID[IDNo])
      radio.send(ID[IDNo])
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
  if message == selfID:
    display.show(Image.HEART)