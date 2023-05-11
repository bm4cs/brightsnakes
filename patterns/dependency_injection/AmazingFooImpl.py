from patterns.dependency_injection import FooInterface


class AmazingFooImpl(FooInterface):
    def do_amazing_thing(self):
        print("I do amazing thing")
