# Написать программу которая в зависимости от вводимых в программу входных параметров
# собирает её выполнение из функций. Программа для расчета траектории движения.
import math

y = 0
x = 0


def Up(a):
    """"Функция описывает движение черепашки по y"""
    if a == 'up' or a == 'UP' or a == 'Up':
        return y
    else:
        return Exception


def Left(a):
    """"Функция описывает движение черепашки по x"""
    if a == 'left' or a == 'LEFT' or a == 'Left':
        return x + 1
    else:
        return Exception


def Right(a):
    """"Функция описывает движение черепашки по x"""
    if a == 'right' or a == 'RIGHT' or a == 'Right':
        return x - 1
    else:
        return Exception


def Down(a):
    """"Функция описывает движение черепашки по y"""
    if a == 'down' or a == 'DOWN' or a == 'Down':
        return y - 1
    else:
        return Exception


n = ''
while n != 'Stop':
    print("Желаете ли вы остановить черевашку. Если да введите Stop")
    n = input()
    print('Если вы хотите чтоб черепашка пошла наверх. Напишите Up. Налево Left. Направо Right. Вниз Down')
    a = input()
    Up(a)
    Left(a)
    Right(a)
    Down(a)
    print('Координаты черепашки')
    print(x, y)
