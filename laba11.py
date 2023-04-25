# Цель работы: Научиться создавать сложные свойства у классов и наследовать другие классы.
# 1. Изменить класс из лабораторной работы № 10 таким образом, чтобы треугольник можно было изменить после создания (заменить точки), но при этом вводимые данные проверялись и при неправильном вводе выводилась ошибка.
# Код создания ошибки:
# raise ValueError('Текст ошибки')  # Ошибка значения
# raise TypeError('Текст ошибки') # Ошибка типа данных
# 2. Добавить функции сравнения треугольников (по площади)
# 3. Создать класс: неизменяемый треугольник на основе треугольника (наследие) так, чтобы нельзя было менять координаты вершин
# 4. Создать класс: прямоугольный треугольник на основе треугольника (наследие) с дополнительной проверкой, что один из углов прямой (проверку можно осуществить с помощью теоремы Пифагора).
# Пример программы, использующей данные классы:
# t = Triangle((1., 0.), (2., 4.), (0., 1.))
# print(t.isosceles()) # False
# print(t.A) # (1., 0.)
# t.B = (0., 0.)
# # t.B = [] # Эта строка выводит TypeError
# print(t) # Треугольник (1.0, 0.0), (0.0, 0.0), (0.0, 1.0)
# print(t.isosceles()) # True
# t2= Triangle((2., 0.), (0., 0.), (0., 1.))
# if t > t2:
# 	print('Первый треугольник больше')
# else:
# 	print('Второй треугольник больше или равен') #Выполняется это условие
# t2 = ImmutableTriangle((1., 0.), (2., 0.), (0., 1.))
# # t2.A = (2., 0.) # Эта строка выводит AttributeError
# t3 = RightTriangle((1., 0.), (0., 0.), (0., 1.))
# # t4 = RightTriangle((1., 0.), (0.25, 0.25), (0., 1.)) # ValueError
# t3.A = (2.,0.)
# # t3.A = (2.,0.5) # Эта строка выводит ValueError (не прямоугольный)

import math


class Triangle:
    """Класс треугольник, свойства и методы"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def lengths(self):
        """Поиск длин сторон треугольника"""
        A = math.sqrt((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2)
        B = math.sqrt((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2)
        C = math.sqrt((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2)
        return A, B, C

    def validate(self):
        """Проверка существования треугольника"""
        A, B, C = self.lengths()
        if A <= 0 or B <= 0 or C <= 0:
            raise ValueError("Значения сторон должны быть положительными.")
        if A + B <= C or A + C <= B or B + C <= A:
            raise ValueError("Треугольника не существует.")

    def medians(self):
        """Находим медианы треугольника"""
        A, B, C = self.lengths()
        ma = 0.5 * math.sqrt(2 * B ** 2 + 2 * C ** 2 - A ** 2)
        mb = 0.5 * math.sqrt(2 * A ** 2 + 2 * C ** 2 - B ** 2)
        mc = 0.5 * math.sqrt(2 * A ** 2 + 2 * B ** 2 - C ** 2)
        return ma, mb, mc

    def heights(self):
        """Находим высоты треугольника"""
        A, B, C = self.lengths()
        s = (A + B + C) / 2
        ha = 2 * math.sqrt(s * (s - A) * (s - B) * (s - C)) / A
        hb = 2 * math.sqrt(s * (s - A) * (s - B) * (s - C)) / B
        hc = 2 * math.sqrt(s * (s - A) * (s - B) * (s - C)) / C
        return ha, hb, hc

    def equilateral(self):
        """Проверяем, является ли треугольник равносторонним"""
        A, B, C = self.lengths()
        return math.isclose(A, B) and math.isclose(A, C) and math.isclose(B, C)

    def isosceles(self):
        """Проверяем, является ли треугольник равнобедренным"""
        A, B, C = self.lengths()
        return math.isclose(A, B) or math.isclose(A, C) or math.isclose(B, C)

    def perimeter(self):
        """Находим периметр треугольника"""
        A, B, C = self.lengths()
        return A + B + C

    def square(self):
        """Находим площадь треугольника по формуле Герона"""
        A, B, C = self.lengths()
        p = (A + B + C) / 2
        return math.sqrt(p * (p - A) * (p - B) * (p - C))

    def rectangular(self):
        """Проверяем, является ли треугольник прямоугольным"""
        A, B, C = sorted(self.lengths())
        return math.isclose(A ** 2 + B ** 2, C ** 2)

    def __eq__(self, other):
        """Сравнение"""
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return True
        else:
            return False

    def lengths2(self):
        """Поиск длин сторон треугольника"""
        A = math.sqrt((self.b[0] - self.c[0]) ** 2 + (self.b[1] - self.c[1]) ** 2)
        B = math.sqrt((self.a[0] - self.c[0]) ** 2 + (self.a[1] - self.c[1]) ** 2)
        C = math.sqrt((self.a[0] - self.b[0]) ** 2 + (self.a[1] - self.b[1]) ** 2)
        return A, B, C

    def medians2(self):
        """Находим медианы треугольника"""
        A, B, C = self.lengths()
        ma = 0.5 * math.sqrt(2 * B ** 2 + 2 * C ** 2 - A ** 2)
        mb = 0.5 * math.sqrt(2 * A ** 2 + 2 * C ** 2 - B ** 2)
        mc = 0.5 * math.sqrt(2 * A ** 2 + 2 * B ** 2 - C ** 2)
        return ma, mb, mc

    def heights2(self):
        """Находим высоты треугольника"""
        A, B, C = self.lengths()
        s = (A + B + C) / 2
        ha = 2 * math.sqrt(s * (s - A) * (s - B) * (s - C)) / A
        hb = 2 * math.sqrt(s * (s - A) * (s - B) * (s - C)) / B
        hc = 2 * math.sqrt(s * (s - A) * (s - B) * (s - C)) / C
        return ha, hb, hc

    def equilateral2(self):
        """Проверяем, является ли треугольник равносторонним"""
        A, B, C = self.lengths()
        return math.isclose(A, B) and math.isclose(A, C) and math.isclose(B, C)

    def isosceles2(self):
        """Проверяем, является ли треугольник равнобедренным"""
        A, B, C = self.lengths()
        return math.isclose(A, B) or math.isclose(A, C) or math.isclose(B, C)

    def perimeter2(self):
        """Находим периметр треугольника"""
        A, B, C = self.lengths()
        return A + B + C

    def square2(self):
        """Находим площадь треугольника по формуле Герона"""
        A, B, C = self.lengths()
        p = (A + B + C) / 2
        return math.sqrt(p * (p - A) * (p - B) * (p - C))

    def rectangular2(self):
        """Проверяем, является ли треугольник прямоугольным"""
        A, B, C = sorted(self.lengths())
        return math.isclose(A ** 2 + B ** 2, C ** 2)


class ImmutableTriangle(Triangle):
    @property
    def P(self):
        return self._P

    @P.setter
    def P(self, P):
        raise AttributeError

    @property
    def O(self):
        return self._O

    @O.setter
    def O(self, O):
        raise AttributeError

    @property
    def H(self):
        return self._H

    @H.setter
    def H(self, H):
        raise AttributeError


triangle = Triangle((7, 5), (8, 6), (10, 8))  # A,B,C соответственно из лаб. работы №2
t2 = Triangle((1, 6), (2, 3), (4, 1))
triangle3 = ImmutableTriangle((1., 0.), (2., 0.), (0., 1.))

medians = triangle.medians()
print("Медианы треугольника:", medians)

heights2 = triangle.heights()
print("Высоты треугольника:", heights2)

equilateral2 = triangle.equilateral()
print("Равносторонний:", equilateral2)

isosceles2 = triangle.isosceles()
print("Равнобедренный:", isosceles2)

perimeter2 = triangle.perimeter()
print("Периметр:", perimeter2)

square = triangle.square()
print("Площадь:", square)

medians2 = triangle.medians2()
print("Медианы треугольника:", medians2)

heights2 = triangle.heights2()
print("Высоты треугольника:", heights2)

equilateral2 = triangle.equilateral2()
print("Равносторонний:", equilateral2)

isosceles2 = triangle.isosceles2()
print("Равнобедренный:", isosceles2)

perimeter2 = triangle.perimeter2()
print("Периметр:", perimeter2)

square2 = triangle.square2()
print("Площадь:", square2)

if triangle == t2:
    print("Треугольники равны")
else:
    print("Треугольники не равны")

if square==square2:
    print("Площади равны")
else:
    print("Площади не равны")

rectangular = triangle.rectangular()
print("Проверка первого треугольника на прямой угол:", rectangular)
rectangular2 = t2.rectangular2()
print("Проверка второго треугольника на прямой угол:", rectangular2)