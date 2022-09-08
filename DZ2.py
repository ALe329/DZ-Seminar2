#    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11


# a = int(input("Введите число: "))
# def s(a):
#     result = 0
#     while a > 0:
#         result += a % 10
#         a //= 10
#     return result
 
# print(s(a))


# print(sum(map(int, list(input("Введите вещественное число: ")))))

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def set_products(n: int) -> list:
#     set = [1]
#     for i in range(2, n+1):
#         set.append(set[-1] * i)
#     return set

# n = int(input('Введите натуральное число: '))
# set = set_products(n)
# print(set)


# n = int(input('Введите число N: '))
# fact = 1
# for i in range(1, n+1):
#      fact *= i
#      print(fact, end=' ')

import random
list = [3.14, 2.63, "Число", 'True ']
random.shuffle(list)
print(list)

