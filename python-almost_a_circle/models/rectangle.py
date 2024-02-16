#!/usr/bin/python3
"""rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """getters"""
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x

    """setters"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @y.setter
    def y(self, value):

        if type(value) is not int:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    @x.setter
    def x(self, value):

        if type(value) is not int:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    def area(self):
        """area of rectangle"""
        return self.height * self.width

    def display(self):
        """display"""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Str Method"""
        str_a = f"({self.id}) {self.x}/{self.y}"
        return f"[Rectangle] {str_a} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the attributtes using args"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary"""
        dictt = {
            "id": self.id,
            "whidth": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dictt
