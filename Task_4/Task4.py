# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


import random
N = int(input ('Введите число N: '))
my_list = []
for i in range (0,N):
    my_list.append (random.randint(-N,N))
mult =1
for i in my_list:
    mult = mult*i
print (mult)
result = list(map(str, my_list))
print (result)
with open (r"C:\Users\77017\OneDrive\Рабочий стол\Python_Home_Work_2\Task_4\test.txt", "w") as file:
    file.write ('\n'.join(result))
file.close()