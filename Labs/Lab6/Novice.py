from microbit import *
import time

class TempSensor:
    def __init__(self, name):
        self.name = name

    def read(self):
        return temperature()

    def display_reading(self):
        temp = self.read()
        display.scroll(str(temp))

    def print_reading(self):
        temp = self.read()
        print(temp)

def main():
    temp_sensor = TempSensor("Temperature")
    start_time = running_time()

    while running_time() - start_time < 40000:
        temp_sensor.display_reading()
        temp_sensor.print_reading()
        sleep(2000)

if __name__ == "__main__":
    main()
