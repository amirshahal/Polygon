# Jether Energy Python Exercise - Amir Shahal - Oct 20th, 2020, file 5 out of 5 files.
from Polygon import Polygon
import unittest
import math


class TestPolygonMethods(unittest.TestCase):
    """A class used for running unit tests on the Polygon class."""

    def test_0_create_empty_polygon(self):
        """Create an empty polygon. Ensure its length is 0."""
        polygon = Polygon()
        self.assertEqual(len(polygon), 0)

    def test_1_index_is_valid(self):
        """Test index's validation"""
        polygon = Polygon()
        with self.assertRaises(Exception):
            # Invalid, we can't insert at 1, only at 0
            polygon.insert((1, 3), 1)

        with self.assertRaises(Exception):
            # Invalid, index must be an integer
            polygon.insert((1, 3), "zero")

        with self.assertRaises(Exception):
            # Invalid, index must be an integer
            polygon.insert((1, 3), None)

        with self.assertRaises(Exception):
            # Invalid, index must be an integer
            polygon.insert((1, 3), 0.2)

        polygon.insert((1, 3), 0)
        with self.assertRaises(Exception):
            # Invalid, index bigger than current length
            polygon.insert((3, 3), 2)

    def test_2_point_is_valid(self):
        """Test point's validation. Point MUST be a 2 dimensional tuple (x,y)"""
        polygon = Polygon()
        with self.assertRaises(Exception):
            polygon.insert((1, ), 0)

        with self.assertRaises(Exception):
            polygon.insert(1, 0)

        with self.assertRaises(Exception):
            polygon.insert((1, "2"), 0)

        with self.assertRaises(Exception):
            polygon.insert(("1", 2), 0)

    def test_3_address_non_existing_point(self):
        """Test addressing non existing Point."""
        polygon = Polygon()
        with self.assertRaises(Exception):
            polygon[0] = (1, 3)

        # Cannot remove an item
        with self.assertRaises(Exception):
            polygon.remove(0)

    def test_4_insert(self):
        """Test insertion"""
        polygon = Polygon()
        polygon.insert((1, 2), 0)
        self.assertTrue(len(polygon) == 1)
        self.assertTrue(polygon[0] == (1, 2))
        self.assertTrue(polygon[0].distance_to_next == 0)
        self.assertTrue(polygon[0].angle == 0)
        self.assertTrue(polygon.get_area() == 0)

    def test_5_addressing(self):
        """Test addressing"""
        polygon = Polygon()
        polygon.insert((1, 2), 0)
        polygon[0] = (8, 9)
        self.assertTrue(polygon[-1] == (8, 9))
        self.assertTrue(polygon[0] == (8, 9))
        self.assertTrue(polygon[0].distance_to_next == 0)
        self.assertTrue(polygon[0].angle == 0)
        self.assertTrue(polygon.get_area() == 0)

    def test_6_iterating(self):
        """Test iterating"""
        polygon = Polygon()
        polygon.insert((0, 1), 0)
        polygon.insert((0, 0), 0)
        polygon.insert((1, 1), 2)
        polygon.insert((1, 0), 3)

        for index, point in enumerate(polygon):
            if index == 0:
                self.assertTrue(point == (0, 0))
                self.assertTrue(point.distance_to_next == 1.0)

            if index == 1:
                self.assertTrue(point == (0, 1))
                self.assertTrue(point.distance_to_next == 1.0)

            if index == 2:
                self.assertTrue(point == (1, 1))
                self.assertTrue(point.distance_to_next == 1.0)

            if index == 3:
                self.assertTrue(point == (1, 0))
                self.assertTrue(point.distance_to_next == 1.0)

    def test_7_distance(self):
        """Test distance after various operations"""
        polygon = Polygon()

        # Test initial distance
        polygon.insert((0, 0), 0)
        self.assertTrue(polygon[0].distance_to_next == 0)

        # Test distance after adding after
        polygon.insert((3, 4), 1)
        self.assertTrue(polygon[0].distance_to_next == 5)
        self.assertTrue(polygon[1].distance_to_next == 5)

        # Test distance after adding before
        polygon.insert((3, -4), 1)
        self.assertTrue(polygon[0].distance_to_next == 5)
        self.assertTrue(polygon[1].distance_to_next == 8)

        # Test distance after []=
        polygon[1] = (1, 1)
        self.assertTrue(polygon[0].distance_to_next == math.sqrt(2))
        self.assertTrue(polygon[1].distance_to_next == math.sqrt(13))

        # Test distance after remove
        polygon.remove(1)
        self.assertTrue(polygon[0].distance_to_next == 5)

    def test_8_angle(self):
        """Test angles calculation and area for non regular triangle."""
        polygon = Polygon()
        polygon.insert((0, 0), 0)
        polygon.insert((1, 1), 1)
        polygon.insert((2, 0), 2)
        self.assertTrue(polygon[0].angle == 45)
        self.assertTrue(polygon[1].angle == 90)
        self.assertTrue(polygon[2].angle == 45)
        self.assertTrue(polygon.get_area() is None)

    def test_9_non_regular_and_regular_polygon(self):
        """Test non regular polygon, then modifying it to a regular one and test again."""
        polygon = Polygon()

        # Single point.
        polygon.insert((1, 2), 0)
        self.assertTrue(polygon[0].distance_to_next == 0)
        self.assertTrue(polygon[0].angle == 0)

        # Two points.
        polygon.insert((2, 2 + math.sqrt(3)), 1)
        self.assertTrue(len(polygon) == 2)
        self.assertAlmostEqual(polygon[0].distance_to_next, 2)
        self.assertTrue(polygon[0].angle == 0)
        self.assertAlmostEqual(polygon[1].distance_to_next, 2)
        self.assertTrue(polygon[1].angle == 0)

        # Non regular triangle.
        polygon.insert((2, 2), 2)
        self.assertTrue(len(polygon) == 3)
        self.assertAlmostEqual(polygon[0].distance_to_next, 2)
        self.assertAlmostEqual(polygon[0].angle, 60.0)

        self.assertAlmostEqual(polygon[1].distance_to_next, math.sqrt(3.0))
        self.assertAlmostEqual(polygon[1].angle, 30.0)

        self.assertAlmostEqual(polygon[2].distance_to_next, 1.0)
        self.assertAlmostEqual(polygon[2].angle, 90.0)

        self.assertTrue(polygon.get_area() is None)

        # Make the triangle regular
        polygon[2] = (3, 2)
        self.assertTrue(len(polygon) == 3)
        self.assertAlmostEqual(polygon[0].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[0].angle, 60.0)

        self.assertAlmostEqual(polygon[1].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[1].angle, 60.0)

        self.assertAlmostEqual(polygon[2].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[2].angle, 60.0)
        self.assertAlmostEqual(polygon.get_area(), math.sqrt(3.0))

    def test_10_square(self):
        """Test a square, regular polygon with edge length of 2"""
        polygon = Polygon()

        polygon.insert((-1, -1), 0)
        polygon.insert((-1, 1), 1)
        polygon.insert((1, 1), 2)
        polygon.insert((1, -1), 3)

        self.assertAlmostEqual(polygon[0].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[0].angle, 90.0)
        self.assertAlmostEqual(polygon[1].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[1].angle, 90.0)
        self.assertAlmostEqual(polygon[2].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[2].angle, 90.0)
        self.assertAlmostEqual(polygon[3].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[3].angle, 90.0)

        self.assertAlmostEqual(polygon.get_area(), 4.0)

    def test_11_rectangle(self):
        """"Test rectangle which has equal 90 degrees angles but non equal edges (hence, not regular)"""
        polygon = Polygon()
        polygon.insert((-5, 0), 0)
        polygon.insert((-2, 0), 1)
        polygon.insert((-2, -2), 2)
        polygon.insert((-5, -2), 3)

        self.assertAlmostEqual(polygon[0].distance_to_next, 3.0)
        self.assertAlmostEqual(polygon[0].angle, 90.0)
        self.assertAlmostEqual(polygon[1].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[1].angle, 90.0)
        self.assertAlmostEqual(polygon[2].distance_to_next, 3.0)
        self.assertAlmostEqual(polygon[2].angle, 90.0)
        self.assertAlmostEqual(polygon[3].distance_to_next, 2.0)
        self.assertAlmostEqual(polygon[3].angle, 90.0)

        self.assertTrue(polygon.get_area() is None)

    def test_12_rhombus(self):
        """"Test rhombus (diamond) which has equal edges but non equal two pairs of equal angles"""
        polygon = Polygon()
        polygon.insert((-1, 0), 0)
        polygon.insert((0, 4), 1)
        polygon.insert((1, 0), 2)
        polygon.insert((0, -4), 3)

        self.assertAlmostEqual(polygon[0].distance_to_next, math.sqrt(17))
        self.assertAlmostEqual(polygon[1].distance_to_next, math.sqrt(17))
        self.assertFalse(polygon[0].angle == polygon[1].angle)
        self.assertAlmostEqual(polygon[0].angle + polygon[1].angle, 180)

        self.assertAlmostEqual(polygon[2].distance_to_next, math.sqrt(17))
        self.assertAlmostEqual(polygon[3].distance_to_next, math.sqrt(17))
        self.assertFalse(polygon[2].angle == polygon[3].angle)
        self.assertAlmostEqual(polygon[2].angle + polygon[3].angle, 180)

        self.assertTrue(polygon.get_area() is None)

    def test_13_regular_pentagon(self):
        polygon = Polygon()
        polygon.insert((0, 1), 0)
        polygon.insert((0.25 * math.sqrt(10 + 2 * math.sqrt(5)), 0.25 * (math.sqrt(5) - 1)), 1)
        polygon.insert((0.25 * math.sqrt(10 - 2 * math.sqrt(5)), -0.25 * (math.sqrt(5) + 1)), 2)
        polygon.insert((-0.25 * math.sqrt(10 - 2 * math.sqrt(5)), -0.25 * (math.sqrt(5) + 1)), 3)
        polygon.insert((-0.25 * math.sqrt(10 + 2 * math.sqrt(5)), 0.25 * (math.sqrt(5) - 1)), 4)

        self.assertAlmostEqual(polygon.get_area(), 2.37764129)


if __name__ == '__main__':
    unittest.main()
