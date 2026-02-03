from microbit import *
import cutebot
import log

# --- Parameters ---
LOG_INTERVAL_MS = 250  # log every 0.25 s
TOTAL_TIME_MS = 40000  # 40 seconds
SAFE_MIN = 20           # cm
SAFE_MAX = 25           # cm

# --- Initialize logging ---
log.set_labels("time_ms", "distance_cm", "action")

start_time = running_time()
next_log = 0

while running_time() - start_time < TOTAL_TIME_MS:
    elapsed = running_time() - start_time
    distance = cutebot.get_sonar_distance()
    
    # Determine action
    if distance < SAFE_MIN:
        cutebot.go_backward()
        action = "backward"
    elif distance > SAFE_MAX:
        cutebot.go_forward()
        action = "forward"
    else:
        cutebot.stop()
        cutebot.set_left_rgb_led(0,255,0)
        cutebot.set_right_rgb_led(0,255,0)
        action = "safe_zone"
    
    # Log every 0.25 s
    if elapsed >= next_log:
        log.add({
            "time_ms": elapsed,
            "distance_cm": distance if distance > 0 else 0,
            "action": action
        })
        next_log += LOG_INTERVAL_MS
    
    sleep(20)

# Turn off LEDs and stop at the end
cutebot.stop()
cutebot.set_left_rgb_led(0,0,0)
cutebot.set_right_rgb_led(0,0,0)
