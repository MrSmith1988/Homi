from microbit import *
import radio
radio.on()

# Change to own name
self_id = "Harry"
ids = ['Brishti', 'Hasini', 'Pratham', 'Jaide', 'Harry',
       'Corrine', 'Aditya', 'Kingston', 'Rupert', 'Ron', 'Pei', 'Smith']


def send():
    list_index = 0

    while True:
        display.scroll(ids[list_index], delay=50)

        if button_a.was_pressed():
            if list_index - 1 >= 0:
                list_index -= 1
            else:
                list_index = len(ids) - 1
        if button_b.was_pressed():
            if list_index + 1 <= len(ids) - 1:
                list_index += 1
            else:
                list_index = 0

        if accelerometer.was_gesture("shake"):
            display.scroll("Sent!")
            radio.send(ids[list_index] + " " + self_id)

            return


while True:
    message = radio.receive()

    if message:
        message_ids = str(message).split()

        if message_ids[0] == self_id:
            display.scroll(message_ids[1] + ":", delay=100)

            display.show(Image.HEART, delay=250)
            sleep(250)
            display.show(Image.HEART, delay=250)
            sleep(250)
    else:
        display.scroll("No Messages", delay=100)

    if button_a.was_pressed() or button_b.was_pressed():
        send()
