import importlib


class DIContainer:
    def __init__(self, config) -> None:
        self.modules = {}
        for key, value in config.items():
            module_name, class_name = value.rsplit('.', 1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            self._modules[key] = cls()

    def get_module(self, key):
        return self._modules[key]
