s = 701
import random
random.seed(s)
seq = tuple(random.random() for r in range(100))
print(seq)
inma = int()
inmi = int()
m1 = []
maxx = seq[0]
minn = seq[0]
sum41 = 0
k = 0
nm = int()
for i in seq:
    if i > maxx:
        maxx = i
        inma = seq.index(i)
    if i < minn:
        minn = i
        inmi = seq.index(i)
print(maxx, inma, "- максимальное значение массива и его номер")
print(minn, inmi, "- минимальное значение массива и его номер")

for i in seq:
    if i > 0.5:
        sum41 += i
    elif i < 0.5:
        m1.append(i)
print(sum41, "- сумма всех элементов массива, больших чем 0.5")
print(m1, "- копия последовательности только с элементами, величина которых меньше 0.5")
for i in seq:
    if 0.7 > i > 0.3:
        k += 1
print(k, "- количество элементов, которые больше 0.3 и меньше 0.7")

for i in seq:
    if i > 0.9:
        nm = seq.index(i)
        break
print(nm, "- номер первого элемента, который больше 0.9")
