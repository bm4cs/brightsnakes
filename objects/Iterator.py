class ParrotIterator:
    def __init__(self, max):
        self._max = max
        self._iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = 2 ** self._iteration

        if value > self._max:
            raise StopIteration

        self._iteration += 1
        return value

    __reversed__ = None
