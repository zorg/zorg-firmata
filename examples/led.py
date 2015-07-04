import zorg
import time

def work (my):
    while True:

        # Toggle the led
        my.led.toggle()
        print("Blink")

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
        "led": {
            "connection": "firmata",
            "driver": "zorg_gpio.Led",
            "pin": 13, # 13 is the on-board LED
        }
    },
    "name": "example", # Give your robot a unique name
    "work": work, # The method (on the main level) where the work will be done
})

robot.start()
