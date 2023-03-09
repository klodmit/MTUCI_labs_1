# Написать программу которая из строки
# иппомом1пр54двполоаплке22ауащра выделяет числа и составляет из них массив
a = "иппомом1пр54двполоаплке22ауащр"
num_list = []

num = ''
for char in a:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))

print(num_list)
