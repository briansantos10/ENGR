from microbit import *
import datalogger
import time

class Sensor:
    def display_reading(self, value):
        display.scroll(str(value))

    def print_reading(self, value):
        print(value)

class TempSensor(Sensor):
    def read(self):
        return temperature()

class LightSensor(Sensor):
    def read(self):
        return display.read_light_level()

# Main loop
def main():
    temp_sensor = TempSensor()
    light_sensor = LightSensor()
    start_time = running_time()

    while running_time() - start_time < 40000:
        # Read sensors
        temp = temp_sensor.read()
        light = light_sensor.read()
        
        # Display readings
        temp_sensor.display_reading(temp)
        temp_sensor.print_reading(temp)
        
        light_sensor.display_reading(light)
        light_sensor.print_reading(light)
        
        datalogger.log(temp, light)
        
        sleep(2000)

if __name__ == "__main__":
    main()
