from microbit import *
def recieveBlink(image):
    def flashImage(image, time):
            display.show(image)
            sleep(time)
            display.clear()
            sleep(time)
    flashImage(image, 200)
    flashImage(image, 200)
    flashImage(image, 400)
    flashImage(image, 200)
    flashImage(image, 200)
    flashImage(image, 400)