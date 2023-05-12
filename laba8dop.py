def move(distance, x, y, direction):
    if direction == 0:  # вправо
        x += distance
    elif direction == 90:  # вверх
        y += distance
    elif direction == 180:  # влево
        x -= distance
    elif direction == 270:  # вниз
        y -= distance

    return x, y

x, y = 0, 0  # начальные координаты черепахи

while True:
    command = input("Введите команду (вверх, вниз, влево, вправо, выход): ").lower()
    while command not in ["вверх", "вниз", "влево", "вправо", "выход"]:
        print("Error")
        command = input("Введите команду (вверх, вниз, влево, вправо, выход): ").lower()

        if command == "выход":
            break

    distance = int(input("Введите расстояние: "))
    if command == "вверх":
        direction = 90
    elif command == "вниз":
        direction = 270
    elif command == "влево":
        direction = 180
    elif command == "вправо":
        direction = 0

    x, y = move(distance, x, y, direction)
    print(f"Позиция черепахи: ({x}, {y})")
