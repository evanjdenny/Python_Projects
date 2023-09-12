class Base:
    """Simple base class with methods."""
    def __init__(self, value):
        self.set_value(value)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

def D