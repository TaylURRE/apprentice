# https://docs.python.org/3/library/unittest.html
import unittest
from milestone3.triangle import Triangle


basicTriangle = Triangle([4, 3, 2])


class TestStringMethods(unittest.TestCase):
    def test_number_sides(self):
        self.assertEqual(basicTriangle.num_sides, 3)

    def test_perimeter(self):
        self.assertEqual(basicTriangle.perimeter(), 4+3+2)

    def test_sides_in_order(self):
        sides = basicTriangle.sorted_sides()
        for index, side in enumerate(sides):
            if(index < 2):
                self.assertTrue(sides[index] > sides[index+1])

    def test_longest_side(self):
        self.assertEqual(basicTriangle.find_longest_side(), 4)

    def test_invalid_triangle(self):
        with self.assertRaises(Exception):
            invalidTriangle0 = Triangle([])
        with self.assertRaises(Exception):
            invalidTriangle1 = Triangle([1])
        with self.assertRaises(Exception):
            invalidTriangle4 = Triangle([1, 2, 3, 4])

    def test_invalid_triangle_where_sides_dont_meet(self):
        with self.assertRaises(Exception):
            invalidTriangle5 = Triangle([1, 2, 5])
            invalidTriangle6 = Triangle([2, 4, 2])
            invalidTriangle7 = Triangle([5, 3, 2])

    def test_calc_area(self):
        special_triangle = Triangle([5,	12, 13])
        area = special_triangle.calc_area()
        self.assertEqual(area, 30)


if __name__ == '__main__':
    unittest.main()
