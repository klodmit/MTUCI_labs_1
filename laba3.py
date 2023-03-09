# i=7, где 7 - номер группы
# j=1, где 1 - номер бригады
# Дано число в формате xxx.xxxx: 57i + 3.4821(j+1)
# Найти сумму цифр целой части и произведение цифр дробной части.
# Вывести исходное число, сумму и произведение в удобным для чтения формате.
# Мое число 583.9642
number = 583.9642
wholesum = 0
productfrac = 1
wholefrac = str(number).split('.')
for i in wholefrac[0]:
    wholesum += int(i[0])
for j in wholefrac[1]:
    productfrac *= int(j[0])
print("Исходное число", number)
print("Сумма цифр целой части", wholesum)
print("Произведение цифр дробной части числа", productfrac)
