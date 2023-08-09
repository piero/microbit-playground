from microbit import *

cross_images = ['00000:00100:01210:00100:00000',
                '00100:01210:12321:01210:00100',
                '00200:02320:23432:02320:00200',
                '00300:03430:34543:03430:00300',
                '00400:04540:45654:04540:00400',
                '00500:05650:56765:05650:00500',
                '00600:06760:67876:06760:00600',
                '00700:07870:78987:07870:00700',
                '00800:08980:89998:08980:00800',
                '00900:09990:99999:09990:00900']

def normalize(value, input_range, output_range) -> float:
    return output_range[0] + ((output_range[1] - output_range[0]) / (input_range[0] - input_range[1])) * (value - input_range[0])

while True:
    sound_level = microphone.sound_level()

    # sound level is [0-255] but brightness is [0-9] => Normalize!
    normalized = int(normalize(sound_level, [0, 255], [0, 9]))
    image = Image(cross_images[normalized])
    display.show(image)
    



    
