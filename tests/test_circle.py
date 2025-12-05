import unittest
import math
from src.circle import perimeter, area

class CircleTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_default_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, math.pi * 10)
    
    def test_negative_perimeter(self):
        res = perimeter(-5)
        self.assertAlmostEqual(res, -math.pi * 10)

    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, math.pi * 3)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_default_area(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25)
    
    def test_negative_area(self):
        res = area(-5)
        self.assertAlmostEqual(res, math.pi * 25)
    
    def test_float_area(self):
        res = area(1.5)
        self.assertAlmostEqual(res, math.pi * 2.25)

if __name__ == '__main__':
    unittest.main()