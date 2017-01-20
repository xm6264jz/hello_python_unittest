import unittest
from triangle import triangle_math


class TestTriangle(unittest.TestCase):

    def test_triangle_area(self):

        # Test area function with some example data
        self.assertEqual(12, triangle_math.area(6, 4))

        # Test with floats
        self.assertAlmostEqual(17.79875, triangle_math.area(7.25, 4.91))


    def test_triangle_with_negative_input(self):

        with self.assertRaises(ValueError):
            triangle_math.area(9, -10)

        with self.assertRaises(ValueError):
            triangle_math.area(-9, 10)

        with self.assertRaises(ValueError):
            triangle_math.area(-9, -10)



    def test_right_angle_triangle(self):

        # Test with some example right-angled triangles
        self.assertTrue(triangle_math.is_right_angle(4, 5, 3))
        self.assertTrue(triangle_math.is_right_angle(7, 24, 25))

        # And some floating-point values
        self.assertTrue(triangle_math.is_right_angle(2.33333333333, 8, 8.3333333333))

        self.assertTrue(triangle_math.is_right_angle(1.22222222222, 6.6666666666, 6.777777777))

        # And non-right-angle triangles
        self.assertFalse(triangle_math.is_right_angle(14, 25, 3))
        self.assertFalse(triangle_math.is_right_angle(3.1, 23.89, 22.4))

        # Test that the order doesn't matter
        self.assertTrue(triangle_math.is_right_angle(4, 5, 3))
        self.assertTrue(triangle_math.is_right_angle(5, 4, 3))
        self.assertTrue(triangle_math.is_right_angle(3, 5, 4))

        #TODO what about zero-length sides?
        #TODO negative lengths?
