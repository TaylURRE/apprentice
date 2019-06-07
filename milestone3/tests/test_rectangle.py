# https://docs.python.org/3/library/unittest.html
import unittest
from milestone3.rectangle import Rectangle


basicRectangle = Rectangle([2, 4, 4, 2])


class TestStringMethods(unittest.TestCase):
    def test_number_sides(self):
        self.assertEqual(basicRectangle.num_sides, 4)

    def test_perimeter(self):
        self.assertEqual(basicRectangle.perimeter(), 4 + 4 + 2 + 2)

    def test_sides_in_order(self):
        sides = basicRectangle.sorted_sides()
        for index, side in enumerate(sides):
            if index < 2:
                self.assertTrue(sides[index] >= sides[index+1])

    def test_longest_side(self):
        self.assertEqual(basicRectangle.find_longest_side(), 4)

    def test_invalid_rectangle(self):
        with self.assertRaises(Exception):
            invalidRectangle0 = Rectangle([])
        with self.assertRaises(Exception):
            invalidRectangle1 = Rectangle([1])
        with self.assertRaises(Exception):
            invalidRectangle4 = Rectangle([1, 2, 3, 4])

    def test_calc_area(self):
        area = basicRectangle.calc_area()
        self.assertEqual(area, 8)


if __name__ == '__main__':
    unittest.main()
