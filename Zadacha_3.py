# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел

#List Comprehension + map

n =int(input())

list1 =[]
fib1 = 1
fib2 = 0

list1 = [i for i in range (0,n)]

listFib=[]
listFibA=[]
listFibB=[]

for g in range(len(list1)):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    listFib.append(fib2)

for h in reversed(listFib) :
    listFibA.append(h)


for q in range (len(listFibA)) :
    b = listFibA[q]*-1
    if q % 2 ==0:
        b=listFibA[q]*-1
    else:
        b=listFibA[q]
    listFibB.append(b)      

print('[',end="")
print(", ".join(map(str, listFibB)),end="")
print(', 0, ',end="")
print(", ".join(map(str, listFib)),end="")
print(']')