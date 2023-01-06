# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))

i = 2
list_num = []

while i <= num:
    if num % i == 0:
        list_num.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(list_num)