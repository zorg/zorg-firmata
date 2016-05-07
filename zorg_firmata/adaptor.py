from zorg.adaptor import Adaptor
from PyMata.pymata import PyMata

import time
import sys
import signal


class Firmata(Adaptor):

    def __init__(self, options):
        super(Firmata, self).__init__(options)

        if 'port' not in options:
            raise self.ParameterRequired(
                'A port must be specified for Firmata connection.'
            )

        self.port = options.get('port')
        self.board = PyMata('/dev/ttyACM0', verbose=True)

        signal.signal(signal.SIGINT, self.signal_handler)

        self.pins = {
            'digital': [],
            'analog': [],
            'pwm': [],
            'servo': [],
            'i2c': [],
        }

    def analog_write(self, pin_number, value):
        if pin_number not in self.pins['analog']:
            self.pins['analog'].append(pin_number)
            self.board.set_pin_mode(
                pin_number,
                self.board.OUTPUT,
                self.board.ANALOG
            )

        self.board.analog_write(pin_number, value)

    def analog_read(self, pin_number):
        if pin_number not in self.pins['analog']:
            self.pins['analog'].append(pin_number)
            self.board.set_pin_mode(
                pin_number,
                self.board.INPUT,
                self.board.ANALOG
            )

        return self.board.analog_read(pin_number)

    def digital_write(self, pin_number, value):
        if pin_number not in self.pins['digital']:
            self.pins['digital'].append(pin_number)
            self.board.set_pin_mode(
                pin_number,
                self.board.OUTPUT,
                self.board.DIGITAL
            )

        self.board.digital_write(pin_number, value)

    def digital_read(self, pin_number):
        if pin_number not in self.pins['digital']:
            self.pins['digital'].append(pin_number)
            self.board.set_pin_mode(
                pin_number,
                self.board.INPUT,
                self.board.DIGITAL
            )

        return self.board.digital_read(pin_number)

    def servo_write(self, pin_number, value):
        if pin_number not in self.pins['servo']:
            self.pins['servo'].append(pin_number)
            self.board.servo_config(pin_number)

        self.board.analog_write(pin_number, value)

    def disconnect(self):
        # Close the firmata interface down cleanly
        self.board.close()

    def signal_handler(sig, frame):
        print('Ctrl+C pressed')
        if self.board is not None:
            self.board.reset()
        sys.exit(0)

    class ParameterRequired(Exception):
        def __init__(self, message='A required parameter was not provided.'):
            super(Firmata.ParameterRequired, self).__init__(message)

        def __str__(self):
            return self.message
