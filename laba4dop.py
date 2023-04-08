# Написать программу
# для замены четных элементов случайного
# массива цифр на первые буквы названия этой цифры
from num2words import num2words
import random
chisla = [random.randint(0, 10) for i in range(10)]
for i in range(len(chisla)):
    if chisla[i]%2==0:
        chisla[i]=num2words(chisla[i])[0:1:]
print(chisla)