from microbit import *

total = 0    
count = 1 

while True:
    display.show(count)
    total += count
    sleep(500)

    if button_b.was_pressed():
        display.scroll("Total:" + str(total))
        break

    count += 1

    # Restart count after 9
    if count > 9:
        number = 1

# Clear the display after exiting
display.clear()
