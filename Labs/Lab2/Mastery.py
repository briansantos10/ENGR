from microbit import *
import random

# 5 most recent reaction times
reaction_times = [] 

while True:
    # Wait some random time between 0.5 and 2.0 seconds
    sleep(random.randint(500, 2000))

    display.show(Image.HEART)

    start_time = running_time()

    # Wait for Button A press
    while not button_a.was_pressed():
        # Check logo 
        if pin_logo.is_touched() and len(reaction_times) > 0:
            fastest = min(reaction_times)
            display.scroll(str(fastest))
            reaction_times.clear()
            display.clear()
            break
        
    else:
        # Button A was pressed
        end_time = running_time()
        reaction = end_time - start_time

        display.scroll(str(reaction))

        # Store reaction time
        reaction_times.append(reaction)

        if len(reaction_times) > 5:
            reaction_times.pop(0)

        display.clear()

    
