# Imports go at the top
from microbit import *
from random import randint

def random_image():
    s = ""
    for row in range(5):
        for col in range(5):
            s = s + str(randint(0, 7))
        s = s + ":"
    return Image(s)
    


# Code in a 'while True:' loop repeats forever
while True:
    image = random_image()
    display.show(image)
    sleep(100)

