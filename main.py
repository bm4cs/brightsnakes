import sys
from socket import socket
from typing import TextIO


class Logger(object):
    def __init__(self, file: TextIO):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()


class SocketLogger(Logger):
    def __init__(self, sock: socket):
        self.sock = sock

    def log(self, message):
        self.sock.sendall(message + '\n'.encode('ascii'))


class FilteredLogger(Logger):
    def __init__(self, pattern: str, file: TextIO):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


def main():
    f = FilteredLogger("Error", sys.stdout)
    f.log('Ignored: this is not important')
    f.log('Error: you really want to see this')


if __name__ == "__main__":
    main()