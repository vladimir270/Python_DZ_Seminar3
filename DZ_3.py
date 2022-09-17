import math
import random
'''
1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

def CheckNumber(): # Проверка на число 
    while True:
        try:
            n = int(input())
            break
        except:
            continue
    return n

def Filllist(some_list, n): #Заполнение списка 
    for i in range(n):
        some_list.append(random.randint(0,30))

print("Введите количество элементов списка:")
namber = CheckNumber()
list1 = []
Filllist(list1, namber)
print(list1)
Summa = 0
for i in range(len(list1)):
    if i%2 != 0:
        Summa += list1[i]
print('Sum =', Summa)


'''
2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
'''

print("Введите количество элементов списка:")
namber = CheckNumber()
list2 = []
Filllist(list2, namber)
print(list2)
list2_new = []
while len(list2) != 0:
    if len(list2) == 1:
        list2_new.append(list2[0]**2)
        break
    else:
        a2 = list2.pop(0)
        b2 = list2.pop()
        list2_new.append(a2*b2)
print(list2_new)




'''
3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
[1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
[4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
'''

list3 = [1.1, 1.2, 3.1, 5.17, 10.02]
list3_new = []
for i in list3:
    list3_new.append(round((i-math.floor(i)), 10))


print(f'Dif = {round(max(list3_new)-min(list3_new), 10)}')


list3new = []
for i in list3:
    list3new.append(str(i).split(".")[1]) 
max_len3 = len(max(list3new, key=len)) 
for i in range(len(list3new)): 
    list3new[i] = int(list3new[i].ljust(max_len3, "0"))
dif3 = int(str(max(list3new)-min(list3new)).rstrip("0")) 

print("Dif =", dif3)

'''
4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
Пример:
45 -> 101101
3 -> 11
2 -> 10
'''

while True:
    print("Введите число для преобразования в двоичную систему")
    namber4 = input("N = ")
    try:
        namber4 = int(namber4)
    except:
        print("Цикл завершен")
        break
    namber4bin = format(namber4, 'b')
    print(f'Number: {namber4bin}, binary: {namber4bin}')


'''
5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
'''
def Fib(n):
    some_listFib = []
    some_listNegoFib = []
    for i in range(0,n):
        if i == 0:
            some_listFib.append(0)
        elif 1 <= i <= 2:
            some_listFib.append(1)
            if i == 1:
                some_listNegoFib.append(1)
            if i == 2:
                some_listNegoFib.append(-1)
        else:
            some_listFib.append(some_listFib[i-2]+some_listFib[i-1])
            some_listNegoFib.append(((-1)**(i+1))*some_listFib[-1])
    
    res = some_listFib.copy()
    while len(some_listNegoFib) != 0:
        a5 = some_listNegoFib.pop(0)
        res.insert(0, a5)
    return res

print("Введите k:")
namber5 = CheckNumber()
list5 = Fib(namber5)
print(list5)