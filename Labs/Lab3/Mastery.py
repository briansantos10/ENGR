from microbit import *

uart.init(baudrate=115200)

light_readings = []
max_seen = 1
freeze = False

def show_bar(level, max_level):
    leds_on = int((level / max_level) * 25)

    img = Image(5, 5)
    for i in range(leds_on):
        x = i % 5
        y = 4 - (i // 5)
        img.set_pixel(x, y, 9)

    display.show(img)

while True:
    light = display.read_light_level()

    # Maintain last 10 readings
    light_readings.append(light)
    if len(light_readings) > 10:
        light_readings.pop(0)

    avg_light = sum(light_readings) / len(light_readings)
    min_light = min(light_readings)
    max_light = max(light_readings)

    if max_light > max_seen:
        max_seen = max_light

    # LED display unless frozen
    if not freeze:
        show_bar(light, max_seen)

    # Serial output
    uart.write(
    "Light:" + str(light) + " Avg:" + str(round(avg_light, 1)) +
    " Min:" + str(min_light) + " Max:" + str(max_light) + "\n"
    )

    # Freeze LED display
    if button_a.was_pressed():
        freeze = True

    # Scroll stats
    if button_b.was_pressed():
        display.scroll(
        "Min:" + str(min_light) + " Max:" + str(max_light) +
        " Avg:" + str(round(avg_light, 1))
        )

    sleep(200)
