from microbit import *
import random as rand

# Track past nums
history = []
while True:
    if accelerometer.was_gesture('shake'):
        num = rand.randint(1,7)
        display.show(num)
        history.append(num)

    # Remove oldest
    if len(history) > 5:
        history.pop(0)

    if( button_a.is_pressed() and button_b.is_pressed()):
        avg = round((sum(history) / len(history)), 1)
        display.scroll("Avg: " + str(avg))
                
        
