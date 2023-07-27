"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self, start = 0):
        self.start = start
        self.current =  start

    def generate(self):
        current_serial = self.current
        self.current += 1
        return current_serial

    def reset(self)
    self.current = self.start

serial = SerialGenerator(start = 100)
print(serial.generate())
print(serialGenerator())
print(serialGenerator())
print(serialGenerator())
reset
print(serialGenerator())