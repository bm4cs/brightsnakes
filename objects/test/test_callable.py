import unittest

from objects.ParrotCallable import ParrotCallable


class TestCallable(unittest.TestCase):
    def test_simple_call(self):
        callable = ParrotCallable()
        result = callable("chomsky", "noam", 123)
        self.assertEqual(1337, result)


if __name__ == '__main__':
    unittest.main()
