from typing import Self


class ParrotCompare:
    def __init__(self, name: str, serial: int):
        self.name = name
        self.serial = serial

    def __eq__(self, other: Self) -> Self:
        return self.serial == other.serial
