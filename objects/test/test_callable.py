import unittest

from objects.ParrotCallable import ParrotCallable


class TestCallable(unittest.TestCase):
    def test_simple_call(self):
        parrot_call = ParrotCallable(1_000, 10_000)
        result = parrot_call("chomsky", "noam", 1930)
        self.assertRegex(result, r"noam chomsky \[1930\] OTP = \d+$")


if __name__ == "__main__":
    unittest.main()
