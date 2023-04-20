# Цель работы: изучить алгоритмы и методы их анализа
# Дано: Массив из 10, 100 и 1000 элементов (s взять из работы № 6)
# import random
# random.seed(s)
# seq10 = [random.random() for _ in range(10)]
# seq100 = [random.random() for _ in range(100)]
# seq1000 = [random.random() for _ in range(1000)]
# Функция сравнения (возвращает True, если x должен быть левее y):
# def comp(x,y): # x, y -- float
# 	return x < y
# Создать функцию, сортирующую список seq по заданной функции сравнения comparator(): [1,2,3,4,5,7,6] - [1,2,3,4,5,6,7]
# def my_sort(seq, comparator):
#  # Ваш код
# Оценить зависимость времени работы от количества элементов массива, например с помощью модуля time.
# Для более точной оценки времени, сортировку следует проводить несколько раз (n) и определить среднее время:
# import time
# start_time = time.time()
# n = 10
# for i in range(n):
#     my_sort(seq10, comp)
# print((time.time() - start_time) / n)
# Сделать выводы.
# Пример работы алгоритма:
# seq = [1, 3, 2]
# def comp(x,y):
# 	return x < y
# my_sort(seq, comp)
# print(seq) # 1, 2, 3
import random
import time

s = 701
random.seed(s)
seq10 = [random.random() for _ in range(10)]
seq100 = [random.random() for _ in range(100)]
seq1000 = [random.random() for _ in range(1000)]


def comp(x, y):  # x, y -- float
    """Функция сравнения"""
    return x < y


def mySort(z, comparator):
    """Функция сортировки реализована через сортировку "пузырьком" """
    for i in range(len(z) - 1):
        for j in range(len(z) - 2, i - 1, -1):
            if comparator(z[j + 1], z[j]):
                z[j], z[j + 1] = z[j + 1], z[j]

    return z


start_time: float = time.time()
n = 10
for i in range(n):
    mySort(seq1000, comp)
    print((time.time() - start_time) / n)
