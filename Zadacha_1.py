# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#List Comprehension

from random import randint

n = 5

list1 = [randint(0, 100) for i in range (1, n+1)]
print(list1)

sum = 0

list2 = [list1[i] for i in range(len(list1)) if i % 2 !=0]
for i in list2:
    sum += i
print(F' сумма элементов на  нечетных позициях : = {sum}')