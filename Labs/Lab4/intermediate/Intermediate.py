from microbit import *
import log
import cutebot

log.set_labels(
    "accel_x",
    "accel_y",
    "accel_z",
    "distance_cm"
)

logging = False

TURN_TIME_MS = 635  
LOG_INTERVAL_MS = 500  

while True:
    if button_a.was_pressed():
        logging = True
        cutebot.go_forward()


    if button_b.was_pressed():
        logging = False
        cutebot.stop()
        break

    if logging:
        ax = accelerometer.get_x()
        ay = accelerometer.get_y()
        az = accelerometer.get_z()
        distance = cutebot.get_sonar_distance()

        log.add({
            "accel_x": ax,
            "accel_y": ay,
            "accel_z": az,
            "distance_cm": distance
        })

        if distance > 0 and distance <= 5:
            cutebot.stop()
            sleep(200)

            cutebot.turn_left()
            sleep(TURN_TIME_MS)

            cutebot.stop()
            sleep(200)

            cutebot.go_forward()

        sleep(LOG_INTERVAL_MS)
