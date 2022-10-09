# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Введите натуральную степень k : "))

coefficient = []
for i in range(1, k + 2):
    coefficient.append(randint(1, 20))

result = []
for i in range(len(coefficient)):
    if k == 1:
        result.append(f'{coefficient[i]}*x')
    elif k == 0:
        result.append(f'{coefficient[i]}')
    else:
        result.append(f'{coefficient[i]}*x**{k}')
    symbol = randint(0, 1)
    if symbol == 1:
        result.append('+')
    elif symbol == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')

record = open('data.txt', 'w')
record.write(''.join(result))
record.close()

print("Проверьте файл data.txt")