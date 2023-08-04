import unittest

from objects.Iterator import ParrotIterator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.parrot_iterator = ParrotIterator(256)

    def test_iterator_basic_reads(self):
        first = 0

        for p in self.parrot_iterator:
            first = p
            break

        self.assertEqual(1, first)
        self.assertEqual(2, next(self.parrot_iterator))
        self.assertEqual(4, next(self.parrot_iterator))

    def test_iterator_exhaustion(self):
        last_value = 0

        for p in self.parrot_iterator:
            last_value = p
            self.assertGreater(p, 0, "all iterator values should be > 0")

        self.assertEqual(256, last_value)


if __name__ == '__main__':
    unittest.main()
