import unittest
from src.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):   
    def test_default_perimeter(self):
        res = perimeter(7, 10)
        self.assertEqual(res, 34)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)    

    def test_float_perimeter(self):
        res = perimeter(3.5, 5.5)
        self.assertAlmostEqual(res, 18.0)
    
    def test_default_area(self):
        res = area(7, 10)
        self.assertEqual(res, 70)

    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_float_area(self):
        res = area(3.5, 5.5)
        self.assertAlmostEqual(res, 19.25)

if __name__ == '__main__':
    unittest.main()