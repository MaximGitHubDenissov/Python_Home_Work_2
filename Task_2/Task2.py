# 2 Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число N  '))
mult = 1
my_list = []
for i in range(1, N+1):
    mult = mult*i
    my_list.append(mult)
print(my_list)
