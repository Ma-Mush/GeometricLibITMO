import unittest
from src.triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):   
    def test_default_perimeter(self):
        res = perimeter(8, 10)
        self.assertEqual(res, 36)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)    

    def test_float_perimeter(self):
        res = perimeter(3.5, 2.5)
        self.assertAlmostEqual(res, 12.0)
    
    def test_default_area(self):
        res = area(8, 10)
        self.assertEqual(res, 80)

    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertAlmostEqual(res, 8.75)

if __name__ == '__main__':
    unittest.main()