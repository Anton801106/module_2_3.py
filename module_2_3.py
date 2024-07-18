# Домашняя работа по уроку "Стиль кода часть II. Цикл While.
# Задача "Нули ничто, отрицание недопустимо!":

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0

while zero < len(my_list):
    if my_list[zero] < 0:
        break
    if my_list[zero] > 0:
        print(my_list[zero])
    zero += 1
