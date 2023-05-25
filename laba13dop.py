# Написать программу, которая должна посчитать за сколько построят дом 20 рабочих если для дома нужно 1.
# привести и залить бетон 2. поставить каркас из балок 3. покрыть облицовкой 4. покрыть крышей.
# Для 1 комнаты нужно 30 кг бетона 20 балок 30 кг облицовки и 10 листов крыши. Расчет для 3-ех этажного 6 комнатного дома.
# на бетон требуется 1 чел.час на 10 кг, на балку 0.5 чел час на балку, 0.5 чел час на 10 кг облицовки, 0.5 чел час на лист
# уровень рабочей силы
worker_efficiency = 20

# кол-во материалов для каждого типа работы в комнате
concrete_volume_per_room = 30
beam_volume_per_room = 20
cladding_volume_per_room = 30
roof_volume_per_room = 10

# кол-во комнат и этажей
room_quantity = 2
floor_quantity = 3

# производительность работы с каждым типом материала
concrete_work_efficiency = 10
beam_work_efficiency = 2
cladding_work_efficiency = 20
roof_work_efficiency = 2

# Время работы с каждым типом материала
concrete_work_time = ((concrete_volume_per_room * 60 / concrete_work_efficiency) / worker_efficiency)
beam_work_time = ((beam_volume_per_room * 60 / beam_work_efficiency) / worker_efficiency)
cladding_work_time = ((cladding_volume_per_room * 60 / cladding_work_efficiency) / worker_efficiency)
roof_work_time = ((roof_volume_per_room * 60 / roof_work_efficiency) / worker_efficiency)

# общее время работы в комнате, на этаже и во всем доме
time_per_room = concrete_work_time + beam_work_time + cladding_work_time
time_per_floor = time_per_room * room_quantity
total_time = time_per_floor * floor_quantity + roof_work_time * room_quantity

hours = int(total_time // 60)
minutes = int(total_time % 60)
print(f'На постройку дома уйдет {hours} часа {minutes} минута')