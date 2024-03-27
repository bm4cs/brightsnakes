import unittest

from objects.ParrotCompare import ParrotCompare


class TestComparer(unittest.TestCase):
    def test_basic_comparison(self):
        freddy = ParrotCompare("freddy", 9872134)
        jenny = ParrotCompare("jenny", 2345544)
        self.assertFalse(freddy == jenny)

        freddy_clone = ParrotCompare("freddy", 9872134)
        self.assertTrue(freddy == freddy_clone)


if __name__ == "__main__":
    unittest.main()
