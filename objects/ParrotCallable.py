import random


class ParrotCallable:
    """
    It's possible to make a class instance callable - exactly like a function - by defining __call__()

    The zipfile module uses this to define a class that can decrypt an encrypted zip file with a given password.
    The zip decryption algorithm requires you to store state during decryption.
    Defining the decryptor as a class allows you to maintain this state within a single instance of the decryptor class.
    he state is initialized in the __init__() method and updated as the file is decrypted.
    But since the class is also “callable” like a function, you can pass the instance to the map() function like so:

    zd = _ZipDecrypter(pwd)
    bytes = zef_file.read(12)
    h = list(map(zd, bytes[0:12]))
    """

    def __init__(self, min, max):
        self._min = min
        self._max = max

    def __call__(self, *args, **kwargs):
        lastname, firstname, id = args
        otp = random.randint(self._min, self._max)
        return f"{firstname} {lastname} [{id}] OTP = {otp}"
