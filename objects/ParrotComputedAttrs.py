class ParrotComputedAttributes:
    """
    Demonstrates the traits a class can implement to define computed attributes.
    That is, attributes and/or methods that are defined dynamically.
    """

    def __getattribute__(self, key):
        if key == "food":
            return "banana"
        else:
            raise AttributeError

    def __getattr__(self, key):
        if key == "name":
            return "polly"
        else:
            raise AttributeError
