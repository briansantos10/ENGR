from microbit import *

 # Store light levels
light_readings = [] 

# 20 light readings
for i in range(20):
    light_readings.append(display.read_light_level())
    sleep(500)  

avg_light = sum(light_readings) / len(light_readings)

currTemp = temperature()

display.scroll("Avg Light: " + str(avg_light) + " Temp: " + str(currTemp))

if avg_light > 100:
    display.scroll("Day")
else:
    display.scroll("Night")
