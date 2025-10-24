# Geometric lib

## В общих словах
Библиотека для выполнения базовых геометрических операций: нахождения площади и периметра круга и квадрата.


## Функции

### Модуль circle: 

Импорт функций: `from geometric_lib.circle import func`

- **`area(r : int | float)`** -> float \
Функция вычисляет площадь круга по его радиусу.
```python3
area(10)  # -> 314.1592653589793
```
- **`perimeter(r : int | float)`** -> float \
Функция вычисляет периметер круга по его радиусу.
```python3
perimeter(10)  # -> 62.83185307179586
```

### Модуль square:
Импорт функций: `from geometric_lib.square import func`

- **`area(a : int | float)`** -> int | float \
Функция вычисляет площадь квадрата по его стороне.
```python3
area(10)  # -> 100
```
- **`perimeter(a : int | float)`** -> float \
Функция вычисляет периметер квадрата по его стороне.
```python3
perimeter(10)  # -> 40
```

## История изменений


| Хеш коммита | Изменения |
|-------------|-----------|
| `d078c8d` | L-03: Docs added |
| `8ba9aeb` | L-03: Circle and square added |