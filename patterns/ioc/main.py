import tomllib

from ioc.DIContainer import DIContainer
from ioc.dependencies.interfaces import FooInterface


class InjectionExample:
    def __init__(self, foo_module: FooInterface) -> None:
        self._foo_module: FooInterface = foo_module

    def do_work(self):
        self._foo_module.do_amazing_thing()


def main():
    with open("config.toml", "rb") as config_file:
        config = tomllib.load(config_file)
        module_config = config["modules"]
        container = DIContainer(module_config)
        foo = container.resolve("foo", FooInterface)
        foo.do_amazing_thing()


if __name__ == "__main__":
    main()
