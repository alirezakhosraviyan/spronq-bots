
class MicroChip:
    """

    """
    value: int = None
    # Overloading operators, because comparison is the most important functionality
    # between Microchips and is so common

    def __init__(self, value: int):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __ne__(self, other):
        return self.value != other.value

    # To multiply two Microchips
    def __mul__(self, other):
        return self.value * other.value

    def __str__(self):
        return str(self.value)
