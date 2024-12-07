# Create a Program

from abc import ABC, abstractmethod


class PC:
    def __init__(self):
        print("PC program starts here")


class Motherboard(ABC):

    @abstractmethod
    def start_motherboard(self):
        pass


class RAM(ABC):

    @abstractmethod
    def start_ram(self):
        pass


class Processor(ABC):
    @abstractmethod
    def start_processor(self):
        pass


class Storage(ABC):
    @abstractmethod
    def store_data(self):
        pass

    @staticmethod
    def load_os():
        print("Loading OS")

    def start_mouse(self):
        print("mouse started")

    def use_headphone(self):
        print("use headphone")

# Class - MotherBoard

# ab → start MotherBoard
#
# Class - RAM
#
# abstractMethod → start ram
#
# Class - Processor
#
# abstractMethod → start processor
#
# Class - Storage
#
# abstractMethod → storage data,
#
# static method
#
# loadOS
#
# non static
#
# startMouse
#
# UseHeadPhone
