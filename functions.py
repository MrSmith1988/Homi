from microbit import *
import radio

arrows = Image('00000:'
               '09090:'
               '90009:'
               '09090:'
               '00000:')

smile = Image('09090:'
              '09090:'
              '00000:'
              '90009:'
              '09990:')

frown = Image('09090:'
              '09090:'
              '00000:'
              '09990:'
              '90009:')

stoneface = Image('00000:'
                  '99099:'
                  '00000:'
                  '09990:'
                  '00000:')

owo = Image('00000:'
            '09090:'
            '00000:'
            '90909:'
            '09090:')

waterpistol = Image('00000:'
                    '99999:'
                    '99999:'
                    '00599:'
                    '00099:')

arrowup = Image('00900:'
                '09990:'
                '99999:'
                '09990:'
                '09990:')

arrowdown = Image('09990:'
                  '09990:'
                  '99999:'
                  '09990:'
                  '00900:')


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


def check_both_buttons() -> tuple:
    """
    Returns a tuple of the states of both button_a and button_b, respectively

    Waits 200 milliseconds before determining the result of whether or not the user has inputted a chord
    """

    def get_buttons():
        """Return the state of button_a and button_b as a tuple, respectively"""

        return (button_a.was_pressed(), button_b.was_pressed())

    buttons_value = get_buttons()

    if True in buttons_value:
        sleep(200)

        new_buttons_value = get_buttons()

    return (buttons_value[0] and new_buttons_value[0], buttons_value[1] and new_buttons_value[1])
