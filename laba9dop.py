# Написать программу которая перебирает массив из 100 случайных элементов и создает
# другой массив из суммы всех предыдущих по элементов.Посчитать сколько времени будет занимать
# каждый следующий шаг и составить из их значений массив

import random
import time

A = [random.randint(1,10) for _ in range(100)] #Исходный случайный массив.
X = [A[0]] #Новый массив, который нам нужен по условию.
T = [] #Массив, в который мы поместим значения времени.

def summa(S):
    Time_start = time.time() #Задаем начало отсчета времени.
    for I in range(0, len(S)-1):
        X.append(X[I] + S[I + 1]) #Добавление в массив элементов, в котором каждый элемент является суммой прошлых.
        Time_end = time.time() #Задаем конец отсчета времени.
        T.append(Time_end - Time_start) #Добавляем значения времени в массив T.
        Time_start = Time_end
    print('Массив, в котором каждый элемент - сумма прошлых:', X)

print('Исходный массив:', A)
summa(A) #Вызов процедуры.
print('Массив с значениями времени:', T)