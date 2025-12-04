import unittest
from src.triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):   
    def test_default_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)    

    def test_float_perimeter(self):
        res = perimeter(3.5, 2.5, 5.5)
        self.assertAlmostEqual(res, 11.5)
    
    def test_default_area(self):
        res = area(8, 10)
        self.assertEqual(res, 40)

    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertAlmostEqual(res, 4.375)

if __name__ == '__main__':
    unittest.main()