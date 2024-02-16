#!/usr/bin/python3
"""class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """init method"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str method."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size values"""
        self.width = value
