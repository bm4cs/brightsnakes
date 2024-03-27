import importlib
from typing import Any, TypeVar

T = TypeVar("T")


class DIContainer:
    def __init__(self, config: dict[str, str]) -> None:
        self._object_map = {}

        for key, value in config.items():
            module_name, class_name = value.rsplit(".", 1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            self._object_map[key] = cls()

    def resolve(self, key: str, _type: T) -> T:
        return self._object_map[key]
