a = 1802890014
print(a, "- исходное число")
s = str(a)
l1 = []
for i in s:
    l1.append(int(i))
print(l1, "- исходный список")
gg = l1.copy()
# Сделать копию списка, в котором заменить элементы на чётных позициях на нечётные и наоборот (с помощью срезов, без циклов)
b = l1[:]
d1 = l1[::2]
d2 = l1[1::2]
# print(d1,"\n",d2)
b[::2] = d2
b[1::2] = d1
print(b, "- список в котором поменяли четные и нечетные позиции")

# Сделать копию списка, в котором поменять порядок элементов на обратный
l3 = gg[::-1]
print(l3, "- список с обратным порядком элементов")


def num(s):
    number = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    return number[s]


print(num(l1[5 - 1]), "- пятый элемент списка")