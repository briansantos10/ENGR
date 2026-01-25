from microbit import *
import datalogger
import microphone

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

class CompassSensor(Sensor):
    def read(self):
        return compass.heading()  # Returns 0-359deg

class SoundSensor(Sensor):
    def read(self):
        return microphone.sound_level()  # Microphone reading

class SensorManager:
    def __init__(self, sensors):
        self.sensors = sensors
        self.logging = False

    def start_logging(self):
        self.logging = True
        print("Logging started")

    def stop_logging(self):
        self.logging = False
        print("Logging stopped")

    def update_sensors(self):
        readings = []
        for sensor in self.sensors:
            value = sensor.read()
            sensor.display_reading(value)
            sensor.print_reading(value)
            readings.append(value)
        if self.logging:
            datalogger.log(*readings)  # Log all readings
        return readings

def main():
    # Create sensor objects
    temp_sensor = TempSensor()
    light_sensor = LightSensor()
    compass_sensor = CompassSensor()
    sound_sensor = SoundSensor()

    # Add sensors to manager
    manager = SensorManager([temp_sensor, light_sensor, compass_sensor, sound_sensor])

    while True:
        if button_a.is_pressed():
            manager.start_logging()
        if button_b.is_pressed():
            manager.stop_logging()
        
        manager.update_sensors()
        sleep(2000)

if __name__ == "__main__":
    main()
