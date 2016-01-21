from zorg.adaptor import Adaptor
from pyfirmata import Board, util


class Firmata(Adaptor):

    def __init__(self, options):
        super(Firmata, self).__init__(options)

        self.port = options.get("port", None)
        self.i2c_ready = False

        layout = options.get("layout", None)
        baudrate = options.get("baudrate", 57600)
        name = options.get("name", None)

        print ">>>", self.port

        if not self.port:
            raise self.ParameterRequired(
                "A port must be specified for Firmata adaptor."
            )

        self.board = Board(
            self.port,
            layout=layout,
            baudrate=baudrate,
            name=name
        )

        self.iterator = util.Iterator(self.board)
        self.iterator.start()

        self.pins = {
            "digital": {},
            "analog": {},
            "pwm": {},
            "i2c": None,
        }

    def pwm_write(self, pin_number, value, period):
        """
        The arduino board doesn't actually support
        analog write. Instead it writes a pwm value.
        """
        if not pin_number in self.pins["analog"]:
            pin = self.board.analog[pin_number]
            self.pins["analog"][pin_number] = pin
        else:
            pin = self.pins["analog"][pin_number]

        pin.write(value)

    def analog_write(self, pin_number, value):
        """
        This calls pwm write with no value for the
        period.
        """
        self.pwm_write(pin_number, value, None)

    def analog_read(self, pin_number):
        if not pin_number in self.pins["analog"]:
            pin = self.board.analog[pin_number]
            self.pins["analog"][pin_number] = pin
        else:
            pin = self.pins["analog"][pin_number]

        pin.enable_reporting()
        return pin.read()

    def digital_write(self, pin_number, value):
        if not pin_number in self.pins["digital"]:
            pin = self.board.digital[pin_number]
            self.pins["digital"][pin_number] = pin
        else:
            pin = self.pins["digital"][pin_number]

        pin.write(value)

    def digital_read(self, pin_number):
        if not pin_number in self.pins["digital"]:
            pin = self.board.analog[pin_number]
            self.pins["digital"][pin_number] = pin
        else:
            pin = self.pins["digital"][pin_number]

        pin.enable_reporting()
        return pin.read()

    class ParameterRequired(Exception):
        def __init__(self, message="A required parameter was not provided."):
            super(Firmata.ParameterRequired, self).__init__(message)

        def __str__(self):
            return self.message
