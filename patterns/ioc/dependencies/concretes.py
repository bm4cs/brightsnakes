from ioc.dependencies.interfaces import FooInterface


class AmazingFooImpl(FooInterface):
    def __init__(self):
        pass

    def do_amazing_thing(self) -> None:
        print("I do amazing thing")
