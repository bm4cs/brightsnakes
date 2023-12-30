import unittest

from objects.ParrotComputedAttrs import ParrotComputedAttributes


class TestComputedAttrs(unittest.TestCase):
    def setUp(self) -> None:
        self._sut = ParrotComputedAttributes()

    def test_read_missing_property(self):
        with self.assertRaises(AttributeError):
            self._sut.missing_property

    def test_getattribute_backed_property(self):
        self.assertEqual("banana", self._sut.food)

    def test_getattr_backed_property(self):
        self.assertEqual("polly", self._sut.name)

if __name__ == '__main__':
    unittest.main()
