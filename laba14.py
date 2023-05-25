# Цель работы: научиться составлять и решать системы линейных уравнений в numpy
# Даны точки на плоскости: (j, j), (j + i, j + 2i), (j + 2i, j - 2i), (j + 3i, 2j - i2), (j + 4i, 2j + i), (j + 5i, 2j - i / 2)
# Найти:
# 1. Многочлен минимальной степень (y = a0 + a1 x + a2 x2 + ...), проходящий через все точки.
# 1а. Определить порядок многочлена (зависит от количества точек)
# 1б. Написать многочлен в общем виде
# 1в. Подставить каждую точку в формулу многочлена, составить систему уравнений.
# 1г. Представить систему уравнений в матричном виде, решить с помощью numpy
# Система уравнений вида:
# Ax = b
# где A -- матрица коэффициентов, b -- матрица результатов, x - матрица неизвестных
# решается с помощью функции:
# x = np.linalg.solve(A, b)
# 2. Записать формулу получившегося многочлена, построить график, сделать выводы.
# Примечание:
# В данной задаче неизвестными являются коэффициенты многочлена, а координаты точек (x и y) известны изначально.
# Для составления системы уравнений удобно представить точки в виде двух одномерных матриц:
#
# И находить различные степени x, возводя первую матрицу в степень поэлементно.
# Важно. Чтобы не возникало переполнения массивов при возведении в большую степень, следует значения точек представить в виде float (например не 60, а 60.0)
# Для составления матрицы коэффициентов системы уравнений можно создать пустую матрицу нужного размера и вставлять в неё нужные элементы:
# A = np.empty((n,n))
# A[:,0]=x
# A[:,1]=x_v_kvadrate
# Для построения графика с помощью библиотеки matplotlib.pyplot можно использовать функции:
# pyplot.plot(x,y) – линия, pyplot.scatter(x,y) – только точки на графике
import numpy as np
import matplotlib.pyplot as plt
# i = 7
# j = 1
# Задание точек
print("Задание точек")
points = np.array([(1, 1), (8, 15), (15, -13), (22,-47), (29,9), (36,-2)])
print(points)
# Определение порядка многочлена
print("Определение порядка многочлена")
n = points.shape[0] - 1
print(n)
# Создание матрицы коэффициентов
print("Создание матрицы коэффициентов")
A = np.empty((n+1, n+1)) # матрица 6*6 случайных элементов
for i in range(n+1):
    A[:,i] = points[:,0]**i # присваиваем каждому столбцу значение 0 столбца матрицы points в котором каждый элемент возведён в степень i и получаем матрицу коэффицентов
print(A)
# Создание матрицы результатов
print("Создание матрицы результатов")
b = points[:,1] # присваиваем переменной b 1 столбец матрицы points
print(b)
# Решение системы уравнений
print("Решение системы уравнений")
x = np.linalg.solve(A, b) # при помощи метода solve получаем матрицу неизвестных
print(x)
# Формула многочлена
poly = np.poly1d(x[::-1]) # получаем многочлен в общем виде
# Вывод многочлена
print("Вывод многочлена")
print(poly)
# График
x_vals = np.linspace(points[0,0], points[-1,0], 100) # генерирует последовательность чисел принимая в себя начальную и конечную точку, а также общее количество точек
y_vals = poly(x_vals) # вычисляет значение функции в соответсвующих точках
plt.scatter(points[:,0], points[:,1]) # расставляет токи на координатной плоскости
plt.plot(x_vals, y_vals) # строит график
plt.show() # выводит рисунок в новом окне
