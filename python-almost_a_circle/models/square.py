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

    def update(self, *args, **kwargs):
        """update atributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary"""
        dictt = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return dictt
