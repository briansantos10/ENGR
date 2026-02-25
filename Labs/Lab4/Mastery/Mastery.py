from microbit import *
import log
import cutebot

SETPOINT_CM = 10
KP = 5
CONTROL_INTERVAL_MS = 100  # 10 Hz

log.set_labels("distance", "error", "velocity")

logging = False

while True:
    if button_a.was_pressed():
        logging = True

    if button_b.was_pressed():
        logging = False
        cutebot.stop()
        break

    if logging:
        distance = cutebot.get_sonar_distance()

        if distance <= 0:
            cutebot.stop()
            sleep(CONTROL_INTERVAL_MS)
            continue

        error = distance - SETPOINT_CM
        velocity = KP * error

        if velocity > 100:
            velocity = 100
        elif velocity < -100:
            velocity = -100

        cutebot.set_motors_speed(int(velocity), int(velocity))

        log.add({
            "distance": distance,
            "error": error,
            "velocity": velocity
        })

        sleep(CONTROL_INTERVAL_MS)
