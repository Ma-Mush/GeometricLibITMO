import unittest

def area(a, b):
    """
    Вычисляет площадь прямоугольника по его длине и высоте.

    Параметры:
        a (число) : Длина прямоугольника.
        b  (число) : Высота прямоугольника.

    Возврат:
        area (число) : Площадь прямоугольника.

    Пример:
        area(10, 5) -> 50
    """

    return a * b


def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника по его длине и высоте.

    Параметры:
        a (число) : Длина прямоугольника.
        b (число) : Высота прямоугольника.

    Возврат:
        perimeter (число): Периметр прямоугольника.

    Пример:
        perimeter(10, 5) -> 30
    """

    return 2 * (a + b)


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
