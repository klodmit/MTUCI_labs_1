s = 701
import random
random.seed(s)
seqs = [[random.random() for r in range(random.randint(1,100))] for r in range(20)]
for seq in seqs:
    if len(seq) % 10 == 1 and len(seq) != 11:
        j = "элемент"
    elif (len(seq) % 10 == 2 or len(seq) % 10 == 3 or len(seq) % 10 == 4) and (len(seq)> 20 or len(seq) < 10):
        j = "элемента"
    else:
        j = "элементов"
    print("В",seqs.index(seq)+1,"массиве",len(seq), j)