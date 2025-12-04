import math
import unittest

def area(r):
    '''
    Вычисляет площадь круга по его радиусу.

    Параметры:
        r (число) :  Радиус круга.
    
    Возврат:
        area (число) : Площадь круга.

    Пример:
        area(10) -> 314.1592653589793
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Вычисляет периметр круга по его радиусу.

    Параметры:
        r (число) :  Радиус круга.
    
    Возврат:
        perimeter (число) : Периметр круга.

    Пример:
        perimeter(10) -> 62.83185307179586
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_default_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, math.pi * 10)
    
    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, math.pi * 3)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_default_area(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25)
    
    def test_float_area(self):
        res = area(1.5)
        self.assertAlmostEqual(res, math.pi * 2.25)
    