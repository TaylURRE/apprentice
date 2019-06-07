from milestone3.heap_sort import run_heap_sort


class Shape:
    """
    A Shape represents an abstract Geometric Shape
    """

    def __init__(self, sides):
        """
        Initializes a new shape with an array
        of side lengths.

        i.e. when sides = [1, 3, 4]
        is a 3-sided shape with side lengths 1, 3, and 4.
        :param sides: an array of side lengths
        """
        self.sides = sides
        self.num_sides = len(sides)
        assert self.num_sides >= 3

    def perimeter(self):
        """
        Returns the sum of a shape's sides
        """
        perimeter = 0
        for index, side in enumerate(self.sides):
            perimeter += side
        return perimeter

    def sorted_sides(self):
        """
        Returns an array of the shape's side lengths,
        sorted length with longest first.

        Stretch goal is to implement the HeapSort
        algorithm covered in the MIT lecture
        """
        sorted_shape_sides = run_heap_sort(self.sides)
        return sorted_shape_sides

    def find_longest_side(self):
        """
        Returns the longest side, ideally in O(1) time
        max returns at O(n) complexity
        """
        longest_side = self.sorted_sides()

        return longest_side[0]
