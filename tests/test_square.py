import unittest
from src.square import perimeter, area

class SquareTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_default_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    
    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 6)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_default_area(self):
        res = area(5)
        self.assertEqual(res, 25)
    
    def test_float_area(self):
        res = area(1.5)
        self.assertAlmostEqual(res, 2.25)

if __name__ == '__main__':
    unittest.main()