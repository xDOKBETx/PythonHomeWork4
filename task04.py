first_number, second_number = int(input("Введите первое число: ")), int(input("Введите второе число: "))

if first_number > second_number:
    big_number = first_number
else:
    big_number = second_number
while True:
    if (big_number % first_number == 0) and (big_number % second_number == 0):
        result = big_number
        break
    big_number += 1
print(result)
