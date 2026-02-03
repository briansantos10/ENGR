from microbit import *
import log
import cutebot

# --- Parameters ---
TOTAL_TIME_MS = 30000       # 30 seconds
LOG_INTERVAL_MS = 500       # 0.5 seconds
CONTROL_INTERVAL_MS = 50    # 50 ms loop for smoother velocity estimation

# --- Initialize logging ---
log.set_labels("time_ms", "velocity")

start_time = running_time()
next_log = 0

# Initial distance reading
prev_distance = cutebot.get_sonar_distance()
if prev_distance < 0:
    prev_distance = 0
prev_time = running_time()

while running_time() - start_time <= TOTAL_TIME_MS:
    current_time = running_time()
    elapsed = current_time - start_time

    # Read current distance
    distance = cutebot.get_sonar_distance()
    if distance < 0:
        distance = prev_distance  # if invalid, use previous

    # Compute velocity (cm/ms)
    delta_t = current_time - prev_time
    if delta_t == 0:
        velocity = 0
    else:
        velocity = (distance - prev_distance) / (delta_t / 1000)  # convert to cm/s

    # Log every 0.5 s
    if elapsed >= next_log:
        log.add({
            "time_ms": int(elapsed),
            "velocity": velocity
        })
        next_log += LOG_INTERVAL_MS

    # Update previous values for next iteration
    prev_distance = distance
    prev_time = current_time

    sleep(CONTROL_INTERVAL_MS)

display.show(Image.HAPPY)

