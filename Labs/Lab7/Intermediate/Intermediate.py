from microbit import *
import cutebot
import log

# --- Parameters ---
NUM_READINGS = 30
INTERVAL_MS = 500  # 0.5 second

# Set CSV column labels
log.set_labels("time_ms", "distance_cm")

# Start logging
start_time = running_time()
for i in range(NUM_READINGS):
    elapsed = running_time() - start_time
    distance = cutebot.get_sonar_distance()
    if distance < 0:  # ignore invalid readings
        distance = 0
    log.add({
        "time_ms": elapsed,
        "distance_cm": distance
    })
    sleep(INTERVAL_MS)

display.show(Image.HAPPY)
