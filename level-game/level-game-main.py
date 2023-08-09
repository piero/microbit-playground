from microbit import *
from random import randint


def normalize(value, input_range, output_range) -> float:
    return output_range[0] + ((output_range[1] - output_range[0]) / (input_range[0] - input_range[1])) * (value - input_range[0])


def animate_win():
    display.show(Image('00000:00600:06960:00600:00000'))
    sleep(50)
    display.show(Image('00600:06960:69696:06960:00600'))
    sleep(50)
    display.show(Image('06960:69696:96069:69696:06960'))
    sleep(50)
    display.show(Image('69696:96069:60006:96069:69696'))
    sleep(50)
    display.show(Image('96069:60006:00000:60006:96069'))
    sleep(50)
    display.show(Image('60006:00000:00000:00000:60006'))
    sleep(50)
    display.clear()



# Set the initial target and initialise score
x_target = randint(0, 4)
y_target = randint(0, 4)
score = 0


while True:    
    x_acc, y_acc, _ = accelerometer.get_values()

    x_acc = min(max(x_acc, -500), 500)
    y_acc = min(max(y_acc, -500), 500)
    
    x_pos = int(abs(normalize(x_acc, [-500, 500], [0, 4])))
    y_pos = int(abs(normalize(y_acc, [-500, 500], [0, 4])))
    
    #print('X: ', x_acc, ' => ', x_pos)
    #print('Y: ', y_acc, ' => ', y_pos)

    if x_pos == x_target and y_pos == y_target:
        # Win! Set a new target
        score += 1
        display.show(score)
        sleep(1000)
        if score < 9:
            animate_win()
            x_target = randint(0, 4)
            y_target = randint(0, 4)
        else:
            # Restart the game
            for _ in range(3):
                animate_win()
            score = 0
    
    display.clear()
    display.set_pixel(x_target, y_target, 5)
    display.set_pixel(x_pos, y_pos, 9)
    sleep(100)
