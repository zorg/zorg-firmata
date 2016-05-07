from unittest import TestCase
from zorg_firmata import Firmata


class ConstructorTests(TestCase):

    def test_no_port(self):
        with self.assertRaises(Firmata.ParameterRequired):
            Firmata({})
