from unittest import TestCase
from zorg_firmata import Firmata
from pyfirmata import mockup
import pyfirmata


class ConstructorTests(TestCase):

    def setUp(self):
        super(ConstructorTests, self).setUp()

        pyfirmata.pyfirmata.serial.Serial = mockup.MockupSerial
        pyfirmata.pyfirmata.BOARD_SETUP_WAIT_TIME = 0

        '''self.firmata = Firmata({
            "port": "somewhere"
        })'''

    def test_no_port(self):
        with self.assertRaises(Firmata.ParameterRequired):
            Firmata({})
