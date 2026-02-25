from microbit import *
import cutebot
import log

LOG_INTERVAL_MS = 250  
TOTAL_TIME_MS = 15000 
BLINK_PERIOD_MS = 200

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

for action, duration in sequence:
    action_start = running_time()
    while running_time() - action_start < duration:
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

        if running_time() - blink_timer >= BLINK_PERIOD_MS // 2:
            blink_state = not blink_state
            if blink_state:
                cutebot.set_right_rgb_led(0,0,255)
                cutebot.set_left_rgb_led(0,0,255)
            else:
                cutebot.set_right_rgb_led(0,0,0)
                cutebot.set_left_rgb_led(0,0,0)
            blink_timer = running_time()

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

        sleep(20)

    cutebot.stop()
    sleep(50)

# Turn off LEDs at the end
cutebot.set_left_rgb_led(0,0,0)
cutebot.set_right_rgb_led(0,0,0)
