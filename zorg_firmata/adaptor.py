from zorg.adaptor import Adaptor
from pyfirmata import Board, util


class Firmata(Adaptor):

    def __init__(self, options):
        super(Firmata, self).__init__(options)

        self.port = options.get("port", None)
        self.i2c_ready = False

        if not self.port:
            raise Exception("No port specified for Firmata adaptor. Cannot proceed")

        self.board = Board(
            self.port,
            layout=None,
            baudrate=57600,
            name=None
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
        The arduino board doesn't actually support analog write.
        Instead they use pwm write.
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
        self.pwm_write(self, pin_number, value, None)

    def analog_read(self, pin_number)
        # NOT TESTED YET
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

    def digital_read(self, pin_number)
        # NOT TESTED YET
        if not pin_number in self.pins["digital"]:
            pin = self.board.analog[pin_number]
            self.pins["digital"][pin_number] = pin
        else:
            pin = self.pins["digital"][pin_number]

        pin.enable_reporting()
        return pin.read()

