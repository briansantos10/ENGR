from microbit import *

while True:
    # Get current temp
    currTemp = temperature()

    if currTemp > 25:
        display.show(Image.HAPPY)
    elif currTemp >= 18: 
        display.show(Image.MEH)
    else:
        display.show(Image.SAD)

    if button_a.was_pressed():
        display.scroll("Temp Check!")

    sleep(2000)


    
