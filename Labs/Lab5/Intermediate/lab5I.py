from microbit import *
import cutebot
import log

# --- Parameters ---
LOG_INTERVAL_MS = 250  # 0.25 seconds
TOTAL_TIME_MS = 15000  # 15 seconds
BLINK_PERIOD_MS = 200  # 5 Hz blink: 100ms on, 100ms off

# --- Initialize log ---
log.set_labels("time_ms", "distance_cm")

# Sequence of movements (action, duration in ms)
sequence = [
    ("forward", 2000),
    ("backward", 2000),
    ("turn_left", 1000),
    ("forward", 2000),
    ("backward", 1000),
    ("turn_right", 1000)
]

start_time = running_time()
next_log = 0
blink_state = False
blink_timer = running_time()

# --- Execute movement sequence ---
for action, duration in sequence:
    action_start = running_time()
    while running_time() - action_start < duration:
        # --- Movement ---
        if action == "forward":
            cutebot.go_forward()
        elif action == "backward":
            cutebot.go_backward()
        elif action == "turn_left":
            cutebot.turn_left()
        elif action == "turn_right":
            cutebot.turn_right()
        else:
            cutebot.stop()

        # --- Blink blue LEDs at 5Hz ---
        if running_time() - blink_timer >= BLINK_PERIOD_MS // 2:
            blink_state = not blink_state
            if blink_state:
                cutebot.set_right_rgb_led(0,0,255)
                cutebot.set_left_rgb_led(0,0,255)
            else:
                cutebot.set_right_rgb_led(0,0,0)
                cutebot.set_left_rgb_led(0,0,0)
            blink_timer = running_time()

        # --- Logging every 0.25s ---
        elapsed = running_time() - start_time
        if elapsed >= next_log:
            distance = cutebot.get_sonar_distance()
            if distance < 0:
                distance = 0
            log.add({
                "time_ms": elapsed,
                "distance_cm": int(distance)
            })
            next_log += LOG_INTERVAL_MS

        sleep(20)  # small delay to reduce CPU usage

    cutebot.stop()
    sleep(50)

# Turn off LEDs at the end
cutebot.set_left_rgb_led(0,0,0)
cutebot.set_right_rgb_led(0,0,0)
