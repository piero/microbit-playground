from microbit import *
from micropython import const

tolerance = const(100)

while True:
    x_strength = accelerometer.get_x()
    y_strength = accelerometer.get_y()
    z_strength = accelerometer.get_z()
    
    x_is_level = -tolerance <= x_strength <= tolerance
    y_is_level = -tolerance <= y_strength <= tolerance
    z_is_level = -1024 - tolerance <= z_strength <= 1024 + tolerance
    
    if x_is_level and y_is_level and z_is_level:
        display.show(Image.HAPPY)
    else:
        display.clear()
