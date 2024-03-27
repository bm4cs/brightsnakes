class ParrotProperties:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        return self._voltage
