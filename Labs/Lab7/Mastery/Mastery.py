from microbit import *
import log

NUM_SAMPLES = 60
INTERVAL_MS = 100  # 0.1 seconds

# Set CSV headers
log.set_labels("time_ms", "sound_level")

start_time = running_time()

for _ in range(NUM_SAMPLES):
    elapsed = running_time() - start_time
    sound = microphone.sound_level()

    log.add({
        "time_ms": elapsed,
        "sound_level": sound
    })

    sleep(INTERVAL_MS)

display.show(Image.HAPPY)
