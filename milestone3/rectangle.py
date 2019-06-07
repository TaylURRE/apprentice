from milestone3.shape import Shape
from milestone3.heap_sort import run_heap_sort


class Rectangle(Shape):
    """
    Represents a 4-sided Shape
    A rectangle has 4 sides, but opposite sides have to be the same length
    """
    def __init__(self, sides):
        Shape.__init__(self, sides)
        sides = self.sides
        side1 = sides[0]
        side2 = sides[1]
        side3 = sides[2]
        side4 = sides[3]

        assert len(sides) == 4

        assert ((side1 == side2 and side4 == side3) or
                (side2 == side3 and side4 == side1) or
                (side1 == side3 and side2 == side4))

    def calc_area(self):
        """
        Returns the area of the rectangle
        :return: area of rectangle

        max returns at O(n) complexity
        min returns at O(n) complexity
        area = min(self.sides) * max(self.sides)
        """

        max_num = self.find_longest_side()
        min_num = self.sorted_sides()[3]

        area = max_num * min_num

        return area
