import zorg
import time

def work (my):
    while True:

        # Check the state of the button
        print("Button is pressed?:", my.button.is_pressed())
        print("Button was bumped?", my.button.is_bumped())

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
        "button": {
            "connection": "firmata",
            "driver": "zorg_gpio.Button",
            "pin": 7, # 7 is a digital pin
        }
    },
    "name": "example", # Give your robot a unique name
    "work": work, # The method where the work will be done
})

robot.start()
