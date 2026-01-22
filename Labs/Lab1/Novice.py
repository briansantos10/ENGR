from microbit import *

#show a smiley face when the board starts
display.show(Image.HAPPY)

#endless while loop
while True:
#scroll your name if button A is pressed
    if button_a.was_pressed():
        display.scroll("Brian")
