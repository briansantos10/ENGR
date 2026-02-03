from microbit import *
import log
import cutebot

# Set CSV column labels
log.set_labels(
    "accel_x",
    "accel_y",
    "accel_z",
    "distance_cm"
)

logging = False

TURN_TIME_MS = 635  # adjust if your robot doesn’t rotate a full 180°
LOG_INTERVAL_MS = 500  # 0.5 seconds (use 100 for 0.1s)

while True:
    # Start logging
    if button_a.was_pressed():
        logging = True
        cutebot.go_forward()


    # Stop logging
    if button_b.was_pressed():
        logging = False
        cutebot.stop()
        break

    if logging:
        # Read sensors
        ax = accelerometer.get_x()
        ay = accelerometer.get_y()
        az = accelerometer.get_z()
        distance = cutebot.get_sonar_distance()

        # Log data
        log.add({
            "accel_x": ax,
            "accel_y": ay,
            "accel_z": az,
            "distance_cm": distance
        })

        # Obstacle detection
        if distance > 0 and distance <= 5:
            cutebot.stop()
            sleep(200)

            # Turn around (180 degrees)
            cutebot.turn_left()
            sleep(TURN_TIME_MS)

            cutebot.stop()
            sleep(200)

            cutebot.go_forward()

        sleep(LOG_INTERVAL_MS)
