from .extra_module import *
from .module import *

print("TEST")


class ToBeTested:
    def __init__(self, data):
        self.data = data

    def reset(self, data):
        self.data = data
