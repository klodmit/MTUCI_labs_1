# Цель работы: научиться создавать и использовать классы.
# Задача. Создать класс Треугольник. Треугольник должен задаваться своими вершинами (3 пары дробных значений).  Должны быть проверки, что значения правильные.
# В классе должны быть реализованы методы нахождения медиан, высот, равнобедренности, равносторонности, площади, периметра. Кроме того, в классе надо реализовать метод вывода треугольника в текстовом виде (например print(treyg)).
# И должна быть функция, определяющая равенство треугольников treyg1 == treyg2 (треугольники равны, если равны длины их сторон). object.__eq__(self, other)
# Проверить работу класса на примере треугольника из лабораторной работы № 2 : Вывести треугольник, медианы, высоты.
# Пример кода, использующего класс Треугольник (значения могут быть не округленные, названия функций и класса могут быть свои):
# t = Triangle((1., 0.), (0., 0.), (0., 1.))
# # t = Triangle([], 'ab', (0.,0.)) # Эта строка выводит TypeError
# print(t.medians()) # (1.118, 1.118, 0.707)
# print(t.heights()) # (1.0, 1.0, 0.707)
# print(t.equilateral()) # False
# print(t.isosceles()) # True
# print(t.perimetr()) # 3.414
# print(t.area()) # 0.5
# t2 = Triangle((1., 0.), (1., 1.), (0., 1.))
# if t == t2:
# 	print('Треугольники равны') #Выполняется это условие
# else:
# 	print('Треугольники   не равны')
# print(t) # Треугольник (1.0, 0.0), (0.0, 0.0), (0.0, 1.0)
# class Triangle():
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

    def __eq__(self, other):
        """Сравнение"""
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return True
        else:
            return False


triangle = Triangle((7, 5), (8, 6), (10, 8))  # A,B,C соответственно из лаб. работы №2
t2 = Triangle((1, 6), (2, 3), (4, 1))

medians = triangle.medians()
print("Медианы треугольника:", medians)

heights = triangle.heights()
print("Высоты треугольника:", heights)

equilateral = triangle.equilateral()
print("равносторонний:", equilateral)

isosceles = triangle.isosceles()
print("равнобедренный:", isosceles)

perimeter = triangle.perimeter()
print("Периметр:", perimeter)

square = triangle.square()
print("Площадь:", square)

if triangle == t2:
    print("Треугольники равны")
else:
    print("Треугольники не равны")
