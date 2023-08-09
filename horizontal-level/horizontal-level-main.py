from microbit import *
from micropython import const

tolerance = const(100)

while True:
    x_is_level = -tolerance <= accelerometer.get_x() <= tolerance
    y_is_level = -tolerance <= accelerometer.get_y() <= tolerance
    z_is_level = (-1024 - tolerance) <= accelerometer.get_z() <= (-1024 + tolerance)
    
    if x_is_level and y_is_level and z_is_level:
        display.show(Image.HAPPY)
    else:
        display.clear()
