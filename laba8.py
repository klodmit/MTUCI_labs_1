# Цель работы. Научиться проверять типы данных.
# Дано. Длины сторон треугольника ненулевой площади (наборы из трёх значений произвольных типов).
# Создать.
# 1. Набор функций, проверяющих правильность заданных наборов (являются ли положительными числами, может ли быть такой треугольник, т.д.)
# 2. Функции, определяющие, является ли треугольник равнобедренным и равносторонним.
# 3. Создать программу, проверяющую треугольник, находящую его равнобедренность и разносторонность в случае успешной проверке, и выводящую результат.
# Ввод длин сторон (точка входа в программу) функции (положительность(positivity) проверка(check) равнобедренность (isosceles) равностороннесть(equilateral) )
# Добавить проверку на разносторонность, сделать проверку ненулевой площади!
import math

a = float(input())
b = float(input())
c = float(input())


def positivity(a, b, c):
    if a and b and c > 0:
        return " All numbers are positive"
    else:
        return "Try another numbers"


def check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "Triangle is exist"
    else:
        return "Try another numbers"


def isoscele(a, b, c):
    if (a == b) or (a == c) or (b == c):
        return "Triangle is isoscele"
    else:
        return "Triangle is not an isoscele"


def equilateral(a, b, c):
    if a == b == c:
        return "Triangle is an equilateral"
    else:
        return "Triangle is not an equilateral"


def S(a, b, c):
    p=(a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    # Площадь будем считать по формуле Герона
    if S > 0: return "S > 0"
    else: return "S <= 0"


print(positivity(a, b, c), "\n",
      check(a, b, c), "\n",
      isoscele(a, b, c), "\n",
      equilateral(a, b, c), "\n",
      S(a,b,c))
