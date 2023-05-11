import toml
from patterns.dependency_injection import FooInterface


class Example:
    def __init__(self, foo_module: FooInterface) -> None:
        self._foo_module: FooInterface = foo_module

    def do_work(self):
        self._foo_module.do_amazing_thing()

def demo():
    toml.load("config.toml")
    foo = 123