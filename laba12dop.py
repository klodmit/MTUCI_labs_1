# Напишите программу, которая генерирует массив из 10 элементов декартовых
# координат и при помощи функций nmPy переводит их в полярные.
# Исходный массив должен содержать точки в 4-ех координатных плоскостях.
# Вывести исходный и полученный массив.
# Угол должен быть в градусах, без отрицательных значений и перекрутов.
import numpy as np

#Функция для генерации массива из 10 случайных декартовых координат
def decart_coords(num_points=10):
    coords = []
    for i in range(num_points):
        x = np.random.uniform(1, 10) * (-1) ** (i % 2)
        y = np.random.uniform(1, 10) * (-1) ** (i // 2)
        coords.append((x, y))
    return np.array(coords)

# Функция для перевода декартовых координат в полярные
def polar_coords(decart_coords):
    polar_coords = []
    for x, y in decart_coords:
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        theta = np.rad2deg(theta)
        if theta < 0:
            theta += 360
            polar_coords.append((r, theta))
    return np.array(polar_coords)

# Генерация массива декартовых координат
decart_coords = decart_coords()

# Перевод декартовых координат в полярные
polar_coords = polar_coords(decart_coords)

# Вывод исходного массива и полученного массива
print("Исходный массив декартовых координат:")
print(decart_coords)
print("\nПолученный массив полярных координат (радиус, угол в градусах):")
print(polar_coords)