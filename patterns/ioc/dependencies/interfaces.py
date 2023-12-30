from abc import ABC, abstractmethod


class FooInterface(ABC):
    @abstractmethod
    def do_amazing_thing(self) -> None:
        raise NotImplementedError()
