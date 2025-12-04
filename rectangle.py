import unittest

def area(length, height):
    """
    Вычисляет площадь прямоугольника по его длине и высоте.

    Параметры:
        length (число) : Длина прямоугольника.
        height  (число) : Высота прямоугольника.

    Возврат:
        area (число) : Площадь прямоугольника.

    Пример:
        area(10, 5) -> 50
    """

    return length * height


def perimeter(length, height):
    """
    Вычисляет периметр прямоугольника по его длине и высоте.

    Параметры:
        length (число) : Длина прямоугольника.
        height  (число) : Высота прямоугольника.

    Возврат:
        perimeter (число): Периметр прямоугольника.

    Пример:
        area(10, 5) -> 30
    """

    return 2 * (length + height)


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
