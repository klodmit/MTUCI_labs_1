import pandas as pd

# список дат в течение недели
dates = pd.date_range(start='2023-05-18', end='2023-05-24', freq='D')

#список дней недели
days_of_week = dates.day_name()

# список времени работы для каждого дня
work_hours = '08:00-17:00'
rest_day = 'Отдых'

# массивы для каждого человека
person1 = [work_hours if 0 <= date.weekday() < 5 else rest_day for date in dates]
person2 = [work_hours if 0 <= date.weekday() < 5 else rest_day for date in dates]
person3 = [work_hours if 0 <= date.weekday() < 5 else rest_day for date in dates]

# словарь с данными
data = {'Дата': dates, 'День недели': days_of_week, 'Человек 1': person1, 'Человек 2': person2, 'Человек 3': person3}

# создаем фрейм pandas
df = pd.DataFrame(data)
df