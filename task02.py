# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

length_list = int(input("Задайте длину списка: "))
enter_list = list()

for i in range(length_list):
    enter_list.append(random.randint(0, 10))

print('Изначальный список:')
print(enter_list)


def get_unique_numbers(x_list):
    exists_list = []

    for number in x_list:
        if number in exists_list:
            continue
        else:
            exists_list.append(number)
    return exists_list


print("Список уникальных чисел: ")
print(get_unique_numbers(enter_list))
