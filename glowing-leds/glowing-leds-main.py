# Imports go at the top
from microbit import *
from random import randint, uniform

heart_image = '04040:44444:44444:04440:00400'
smile_image = '00000:04040:00000:40004:04440'
diamond_image = '00400:04040:40004:04040:00400'
glow_speed_ms = 80

def random_image() -> str:
    s = ''
    for row in range(5):
        for col in range(5):
            if uniform(0., 10.) >= 7.5: # set LED with 75% probability
                s = s + str(randint(3, 7))
            else:
                s = s + '0'
        s = s + (':' if row < 4 else '') # don't append ':' to the end
    #print(s)  # print image string to serial output
    return s

def glow_led(led: str, increment: int, increasing: bool, preserve_off: bool) -> str:
    if (led == ':') or (led == '0' and preserve_off):
        return led
    else:
        led_value = int(led)
        if increasing:
            led_value = min(led_value + increment, 9)
        else:
            led_value = max(led_value - increment, 0)
        return str(led_value)

def glow(img: str, increment: int, increasing: bool, preserve_off: bool) -> str:
    return ''.join([glow_led(led, increment, increasing, preserve_off) for led in img])


# Code in a 'while True:' loop repeats forever
while True:
    # set the image to display
    img = random_image()
    if button_a.was_pressed():
        img = heart_image
    if button_b.was_pressed():
        img = diamond_image
    if accelerometer.was_gesture('shake'):
        img = smile_image

    display.show(Image(img))
    
    # increase glow
    for _ in range(5):
        img = glow(img, 1, True, True)
        display.show(Image(img))
        sleep(glow_speed_ms)
    
    # decrease glow
    for _ in range(9):
        img = glow(img, 1, False, True)
        display.show(Image(img))
        sleep(glow_speed_ms)

    sleep(500)
