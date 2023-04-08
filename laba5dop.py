# Напишите программу, каторая проверяет
# введеные данные в input на соответствие
# формату float и если выводит в случае успеха true
a=input()
try:
    float(a)
    print(True)
except ValueError:
    print(False)
