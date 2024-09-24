from abc import ABC, abstractmethod
import math

class Figure(ABC):
    def __init__(self, center: tuple):
        self._center = center
    
    @property
    def center(self):
        return self._center
    
    @center.setter
    def center(self, new_center: tuple):
        self._center = new_center
    
    def translate(self, a: float, b: float):
        """Move the figure by (a, b)."""
        self._center = (self._center[0] + a, self._center[1] + b)

    @property
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass

    @property
    @abstractmethod
    def area(self):
        """Calculate the area."""
        pass

    @abstractmethod
    def grow_area(self, factor: float):
        """Grow the area by a given factor."""
        pass

    @abstractmethod
    def grow_perimeter(self, factor: float):
        """Grow the perimeter by a given factor."""
        pass

    @abstractmethod
    def vertices(self):
        """Return the vertices of the figure."""
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} - Perimeter: {self.perimeter}, Area: {self.area}, Center: {self.center}"

class Rectangle(Figure):
    def __init__(self, center: tuple, length: float, width: float):
        super().__init__(center)
        self.length = length
        self.width = width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    @property
    def area(self):
        return self.length * self.width

    def grow_area(self, factor: float):
        """Grow the area by a factor, adjusting length and width proportionally."""
        scaling_factor = math.sqrt(factor)
        self.length *= scaling_factor
        self.width *= scaling_factor

    def grow_perimeter(self, factor: float):
        """Grow the perimeter by a proportional amount, adjusting length and width."""
        scaling_factor = factor / self.perimeter
        self.length *= (1 + scaling_factor)
        self.width *= (1 + scaling_factor)

    def vertices(self):
        """Return the four vertices of the rectangle."""
        x, y = self.center
        half_length = self.length / 2
        half_width = self.width / 2
        return [
            (x - half_length, y - half_width),  # Bottom-left
            (x + half_length, y - half_width),  # Bottom-right
            (x + half_length, y + half_width),  # Top-right
            (x - half_length, y + half_width)   # Top-left
        ]

class EquilateralTriangle(Figure):
    def __init__(self, center: tuple, side: float):
        super().__init__(center)
        self.side = side

    @property
    def perimeter(self):
        return 3 * self.side

    @property
    def area(self):
        return (math.sqrt(3) / 4) * (self.side ** 2)

    def grow_area(self, factor: float):
        """Grow the area by a factor, adjusting the side proportionally."""
        scaling_factor = math.sqrt(factor)
        self.side *= scaling_factor

    def grow_perimeter(self, factor: float):
        """Grow the perimeter by a proportional amount, adjusting the side."""
        scaling_factor = factor / self.perimeter
        self.side *= (1 + scaling_factor)

    def vertices(self):
        """Return the three vertices of the equilateral triangle."""
        x, y = self.center
        h = (math.sqrt(3) / 2) * self.side
        half_base = self.side / 2
        return [
            (x - half_base, y - h / 3),  # Bottom-left
            (x + half_base, y - h / 3),  # Bottom-right
            (x, y + 2 * h / 3)           # Top
        ]
        # Example usage:
# Creating a rectangle and a triangle
rectangle = Rectangle((0, 0), 4, 2)
triangle = EquilateralTriangle((0, 0), 3)

# Printing the objects
print(rectangle)  # Rectangle - Perimeter: 12, Area: 8, Center: (0, 0)
print(triangle)   # EquilateralTriangle - Perimeter: 9, Area: 3.8971143170299753, Center: (0, 0)

# Translating the rectangle
rectangle.translate(2, 3)
print(rectangle)  # Center should now be (2, 3)

# Growing the area of the triangle by a factor of 4 (side increases proportionally)
triangle.grow_area(4)
print(triangle)   # Area should now be 4 times larger

# Getting the vertices of the rectangle and triangle
print("Rectangle vertices:", rectangle.vertices())
print("Triangle vertices:", triangle.vertices())