from microbit import *
import log
import cutebot

# --- Proportional control parameters ---
SETPOINT_CM = 10
KP = 5
CONTROL_INTERVAL_MS = 100  # 10 Hz

# Logging labels (must match assignment exactly)
log.set_labels("distance", "error", "velocity")

logging = False

while True:
    # Start control + logging
    if button_a.was_pressed():
        logging = True

    # Stop control + logging
    if button_b.was_pressed():
        logging = False
        cutebot.stop()
        break

    if logging:
        # Read distance
        distance = cutebot.get_sonar_distance()

        # Ignore invalid sonar readings
        if distance <= 0:
            cutebot.stop()
            sleep(CONTROL_INTERVAL_MS)
            continue

        # Compute proportional control
        error = distance - SETPOINT_CM
        velocity = KP * error

        # Clamp velocity
        if velocity > 100:
            velocity = 100
        elif velocity < -100:
            velocity = -100

        # Apply velocity to both wheels
        cutebot.set_motors_speed(int(velocity), int(velocity))

        # Log data
        log.add({
            "distance": distance,
            "error": error,
            "velocity": velocity
        })

        sleep(CONTROL_INTERVAL_MS)
