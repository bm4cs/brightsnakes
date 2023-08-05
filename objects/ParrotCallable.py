class ParrotCallable:
    """
    It's possible to make a class instance callable - exactly like a function - by defining __call__()
    """
    def __call__(self, *args, **kwargs):
        lastname, firstname, id = args
        return 1337
