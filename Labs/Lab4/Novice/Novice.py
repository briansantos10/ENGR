from microbit import *
import log

# Logging labels
log.set_labels("light", "temp")
logging = False

while True:
    # Start logging
    if button_a.was_pressed():
        logging = True

    # Stop logging
    if button_b.was_pressed():
        logging = False
        break

    if logging:
        light = display.read_light_level()
        temp = temperature()

        log.add({
            "light": light,
            "temp": temp
        })

        sleep(500)  # 0.5 seconds

