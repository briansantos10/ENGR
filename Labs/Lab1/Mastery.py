from microbit import *

# Inital min and max
minLight = 255
maxLight = 0

while True:
    currLightLvl = display.read_light_level()

    # Update min and max
    if currLightLvl < minLight:
        minLight = currLightLvl
    if currLightLvl > maxLight:
        maxLight = currLightLvl

    display.scroll("L:" + str(currLightLvl))

    if currLightLvl > 180:
        display.show(Image.HAPPY)
    elif currLightLvl >= 100:
        display.show(Image.MEH)
    else:
        display.show(Image.SAD)

    if button_b.was_pressed():
        display.scroll("Min:" + str(minLight))
        display.scroll("Max:" + str(maxLight))

    sleep(2000)
