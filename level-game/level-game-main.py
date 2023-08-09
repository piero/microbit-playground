from microbit import *
from random import randint


def normalize(value, input_range, output_range) -> float:
    return output_range[0] + ((output_range[1] - output_range[0]) / (input_range[0] - input_range[1])) * (value - input_range[0])


# Set the initial target
x_target = randint(0, 4)
y_target = randint(0, 4)


while True:    
    x_acc = accelerometer.get_x()
    y_acc = accelerometer.get_y()

    x_acc = min(max(x_acc, -500), 500)
    y_acc = min(max(y_acc, -500), 500)
    
    x_pos = int(abs(normalize(x_acc, [-500, 500], [0, 4])))
    y_pos = int(abs(normalize(y_acc, [-500, 500], [0, 4])))
    
    #print('X: ', x_acc, ' => ', x_pos)
    #print('Y: ', y_acc, ' => ', y_pos)

    if x_pos == x_target and y_pos == y_target:
        # Win! Set a new target
        display.show(Image.TARGET)
        sleep(1000)
        x_target = randint(0, 4)
        y_target = randint(0, 4)
    
    display.clear()
    display.set_pixel(x_target, y_target, 5)
    display.set_pixel(x_pos, y_pos, 9)
    sleep(100)
