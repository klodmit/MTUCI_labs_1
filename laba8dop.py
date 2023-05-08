# Написать программу которая в зависимости от вводимых в программу входных параметров
# собирает её выполнение из функций. Программа для расчета траектории движения.
import math

import math

y = 0
x = 0


def Up(a):
    if a == 'up' or a == 'UP' or a == 'Up':
        global y
        y = y + 1
    else:
        Exception


def Left(a):
    if a == 'left' or a == 'LEFT' or a == 'Left':
        global x
        x = x - 1

    else:
        Exception


def Right(a):
    if a == 'right' or a == 'RIGHT' or a == 'Right':
        global x
        x = x + 1

    else:
        Exception


def Down(a):
    if a == 'down' or a == 'DOWN' or a == 'Down':
        global y
        y = y - 1
    else:
        Exception


n = ''
while n != 'Stop':
    print("Желаете ли вы остановить черевашку. Если да введите Stop")
    n = input()
    print('Если вы хотите чтоб черепашка пошла наверх. Напишите. Налево Left. Направо Right. Вниз Down')
    a = input()

    Right(a)
    Down(a)
    Up(a)
    Left(a)

    print('Координаты черепашки')
    print(x, y)
