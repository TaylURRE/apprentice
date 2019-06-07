from milestone3.shape import Shape


class Triangle(Shape):
    """
    Represents a 3-sided Shape
    Sum of two sides must be greater than 3rd side
    """
    def __init__(self, sides):
        Shape.__init__(self, sides)
        sides = self.sides
        side1 = self.sides[0]
        side2 = self.sides[1]
        side3 = self.sides[2]

        assert len(sides) == 3
        assert side1 + side2 > side3
        assert side2 + side3 > side1
        assert side1 + side3 > side2

    def calc_area(self):
        """
        sp - semiperimeter
        area = square root of |sp(sp-side1)(sp-side2)(sp-side3)|
        Returns the area of the triangle
        :return: area of triangle
        """
        i = 1
        perimeter = self.perimeter()
        sp = perimeter/2.0

        for side in self.sides:
            i *= (sp-side)

        area = (sp * i)**(1/2.0)
        return area
