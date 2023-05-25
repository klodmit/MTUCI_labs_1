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

def length(ax,bx,ay,by):
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5

class triangle():
    """треугольник и действия с ним"""
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3
        self.type_check()
        self.checking_coordinates()
    def __str__(self):
        return f'({self._x1}, {self._y1}, {self._x2}, {self._y2}, {self._x3}, {self._y3})'
    def type_check(self):
        if (type(self._x1) == float) and (type(self._x2) == float) and (type(self._x3) == float) and (type(self._y1) == float) and (type(self._y2) == float) and (type(self._y3) == float):
            return True
        else:
            raise TypeError('Неправильный тип треугольника')
    def checking_coordinates(self):
        if (self._x1 == self._x2 and self._y1 == self._y2) or (self._x1 == self._x3 and self._y1 == self._y3) or (self._x2 == self._x3 and self._y2 == self._y3):
            raise ValueError('Ошибка значения')
        else:
            return True
    def l12(self):
        return length(self._x1, self._x2, self._y1, self._y2)
    def l23(self):
        return length(self._x2, self._x3, self._y2, self._y3)
    def l13(self):
        return length(self._x1, self._x3, self._y1, self._y3)
    def __eq__(self, other):
        return self.l12() == other.l12() and self.l23() == other.l23() and self.l13() == other.l13()
    def medd(self):
        # двойной индекс обозначает положение точки на стороне между точками с соответствующими одинарными соседними индексами
        # например (x12,y12) координаты некоторой точки на стороне между точками (x1,y1) и (x2,y2)
        x12 = (self._x1 + self._x2) / 2 # вычисления координат середины отрезка
        y12 = (self._y1 + self._y2) / 2
        x13 = (self._x1 + self._x3) / 2
        y13 = (self._y1 + self._y3) / 2
        x23 = (self._x2 + self._x3) / 2
        y23 = (self._y2 + self._y3) / 2
        med1 = length(self._x1, x23, self._y1, y23)
        med2 = length(self._x2, x13, self._y2, y13)
        med3 = length(self._x3, x12, self._y3, y12)
        return round(med1,3), round(med2,3), round(med3,3)
    def perimetr(self):
        l12 = self.l12()
        l23 = self.l23()
        l13 = self.l13()
        p = l12 + l13 + l23
        return round(p,3)
    def area(self):
        p2 = self.perimetr() / 2  # полупериметр
        s = (p2 * (p2 - self.l12()) * (p2 - self.l13()) * (p2 - self.l23())) ** 0.5  # площадь по формуле Герона
        return round(s,0)
    def __gt__(self, other):
        return self.area() > other.area()
    def high(self):
        h1 = (2 * self.area()) / self.l23() # длина высоты опущенной из точки (x1,y1)
        h2 = (2 * self.area()) / self.l13()
        h3 = (2 * self.area()) / self.l12()
        return round(h1,3), round(h2,3), round(h3,3)
    def equilateral(self):
        return self.l23() == self.l12() == self.l13()

    def isosceles(self):
        if self.equilateral():
            return True
        return (self.l23() == self.l12()) or (self.l12() == self.l13()) or (self.l23() == self.l13())
    # перегрузка функции
    @property
    def A(self):
        return self._x1, self._y1

    @A.setter
    def A(self, d1=tuple()):
        if type(d1[0]) == type(d1[1]) == float:
            self._x1 = d1[0]
            self._y1 = d1[1]
        else:
            raise TypeError('Неправильный тип треугольника')

    @property
    def B(self):
        return self._x2, self._y2

    @B.setter
    def B(self, d2=tuple()):
        if type(d2[0]) == type(d2[1]) == float:
            self._x2 = d2[0]
            self._y2 = d2[1]
        else:
            raise TypeError('Неправильный тип треугольника')

    @property
    def C(self):
        return self._x3, self._y3

    @C.setter
    def C(self, d3=tuple()):
        if type(d3[0]) == type(d3[1]) == float:
            self._x3 = d3[0]
            self._y3 = d3[1]
        else:
            raise TypeError('Неправильный тип треугольника')

class immutabletriangle(triangle):
    """неизменяемый треугольник"""
    @property
    def A(self):
        return self._x1, self._y1

    @property
    def B(self):
        return self._x2, self._y2

    @property
    def C(self):
        return self._x3, self._y3

class rectriangle(triangle):
    """прямоугольный треугольник"""
    def __init__(self,x1,y1,x2,y2,x3,y3):
        super().__init__(x1,y1,x2,y2,x3,y3)
        self.checking_rectangular()
    def checking_rectangular(self):
        l12 = self.l12()
        l23 = self.l23()
        l13 = self.l13()
        jag = [l12, l13, l23]
        jag.sort()
        self._gip = jag[2]  # гипотенуза
        self._kat1 = jag[1]  # катет
        self._kat2 = jag[0]  # катет
        if (abs(self._gip ** 2 - ((self._kat1 ** 2) + (self._kat2 ** 2))) > 0.000000000001):
            if (self._gip ** 2 != (self._kat1 ** 2) + (self._kat2 ** 2)):
                raise ValueError('не прямоугольный треугольник')

    @property
    def A(self):
        return self._x1, self._y1

    @property
    def B(self):
        return self._x2, self._y2

    @property
    def C(self):
        return self._x3, self._y3

    @A.setter
    def A(self, d3=tuple()):
        if type(d3[0]) == type(d3[1]) == float:
            self._x1 = d3[0]
            self._y1 = d3[1]
            self.checking_rectangular()
        else:
            raise TypeError('Неправильный тип треугольника')

    @B.setter
    def B(self, d3=tuple()):
        if type(d3[0]) == type(d3[1]) == float:
            self._x2 = d3[0]
            self._y2 = d3[1]
            self.checking_rectangular()
        else:
            raise TypeError('Неправильный тип треугольника')

    @C.setter
    def C(self, d3=tuple()):
        if type(d3[0]) == type(d3[1]) == float:
            self._x3 = d3[0]
            self._y3 = d3[1]
            self.checking_rectangular()
        else:
            raise TypeError('Неправильный тип треугольника')

t1 = triangle(11.,4.,7.,8.,3.,4.)
t2 = triangle(11.,4.,11.,5.,3.,4.)
print(t1.medd(),"- медианы")
print(t1.high(),"- высоты")
print(t1.perimetr(),"- периметр")
print(t1.area(),"- площадь")
print("равносторонний -",t1.equilateral())
print("равнобедренный -",t1.isosceles())
print("---------------------------------------")
print(t2.medd(),"- медианы")
print(t2.high(),"- высоты")
print(t2.perimetr(),"- периметр")
print(t2.area(),"- площадь")
print("равносторонний -",t2.equilateral())
print("равнобедренный -",t2.isosceles())
print("---------------------------------------")
if t2 == t1:
    print("Треугольники равны")
else:
    print("Треугольники не равны")
print("---------------------------------------")
if t1 > t2:
    print('Первый треугольник больше')
else:
    print('Второй треугольник больше или равен')
print("---------------------------------------")
print(t1.A,t1.B,t1.C)
t1.A = (12.0, 7.0)
t1.B = (5.0, 3.0)
t1.C = (9.0, 6.0)
print(t1.A,t1.B,t1.C)
print("---------------------------------------")
t3 = rectriangle(2.,4.,2.,7.,5.,4.)
# t3.A = (12.0, 7.0)
print(t3)
print("---------------------------------------")
t4 = immutabletriangle(3.,6.,4.,8.,5.,7.)
# t4.A = (9.0, 4.0)
print(t4.A,t4.B,t4.C)
print("---------------------------------------")
print(t1, "- 1 треугольник")
print(t2, "- 2 треугольник")
print(t3, "- 3 треугольник")
print(t4, "- 4 треугольник")
