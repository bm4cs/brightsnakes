import unittest

from objects.Parrot import Parrot


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_default_voltage(self):
        # print("running test test_default_voltage")
        polly = Parrot()
        self.assertEqual(100_000, polly.voltage)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()

# python3 -m unittest -v objects/test/test_parrot.py
# python3 -m unittest objects.test.test_parrot.MyTestCase.test_default_voltage
