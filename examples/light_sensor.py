import zorg
import time

def work (my):
    while True:

        # Toggle the led
        print("Reading:", my.light_sensor.read())

        if my.light_sensor.has_changed():
            print("Light sensor reading has changed past threshold.")
        else:
            print("Light sensor reading unchanged.")

        # Wait 1 second before doing it again
        time.sleep(1)

robot = zorg.robot({
    "connections": {
        "firmata": {
            "adaptor": "zorg_firmata.Firmata",
            "port": "/dev/ttyUSB0",
        },
    },
    "devices": {
        "light_sensor": {
            "connection": "firmata",
            "driver": "zorg_gpio.LightSensor",
            "pin": 5, # 5 is an analog pin
        }
    },
    "name": "example", # Give your robot a unique name
    "work": work, # The method where the work will be done
})

robot.start()
