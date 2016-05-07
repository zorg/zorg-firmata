import zorg
import time

def work(my):
    while True:

        # Move the servo to 20 degrees
        my.servo.set_angle(20)

        print("Servo angle set to", my.servo.get_angle())

        # Wait 1 seconds before doing it again
        time.sleep(1)

        # Move the servo to 100 degrees
        my.servo.set_angle(100)

        print("Servo angle set to", my.servo.get_angle())

        # Wait 1 seconds before doing it again
        time.sleep(1)

robot = zorg.robot({
    "connections": {
        "ArduinoLeonardo": {
            "adaptor": "zorg_firmata.Firmata",
            "port": "/dev/ttyACM0",
        },
    },
    "devices": {
        "servo": {
            "connection": "ArduinoLeonardo",
            "driver": "zorg_grove.Servo",
            "pin": 9, # 9 is a pwm pin
        }
    },
    "name": "Servo Robot", # Give your robot a unique name
    "work": work, # The method where the work will be done
})

robot.start()
