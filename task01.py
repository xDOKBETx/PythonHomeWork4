# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factor(n):
    multiplier_list = []
    x = 2
    while x * x <= n:
        if n % x == 0:
            multiplier_list.append(x)
            n //= x
        else:
            x += 1
    if n > 1:
        multiplier_list.append(n)
    return multiplier_list


print(prime_factor(int(input("Введите число N: "))))
