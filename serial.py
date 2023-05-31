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
    def __init__(self,start=0):
        self.start = start
        self.current = start
    
    def generate(self):
        "Generate new serial number from start number passed in, increment current number each time generate is called"
        self.current +=1
        # print(self.current)
        return  self.current

    def reset(self):
        "Reset the serial number back to the original start number passed in"
        self.current = self.start
        # print(self.current)
        return self.current
    
    def __str__(self):
        return f"SerialGenerator with start number at {self.start} and current number at {self.current}"
    
    def __repr__(self) -> str:
        return f"SerialGenerator(start={self.start})"
    

serial = SerialGenerator(start=100)
print(serial)

        

