print('Срез в диапазоне позиций в Python')
txt = '12345'
print(txt[1:-1])

lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[0:3])

print(lst[1:5])

print(lst[1:6])
print()

print('Срез от позиции в Python')
txt = '12345'
print(txt[1:])

lst = ['ab', 1, 'cd', 2, 'ef', 3, 4]
print(lst[3:])
print()

print('Срез до позиции в Python')
txt = '12345'
print(txt[:-1])

lst = ['a', 'b', 'c', 'd', 'e']
print(lst[:2])
print()

print('Срез с отрицательными позициями в Python')
txt = '123456789'
print(txt[4:-2])

lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(lst[1:-2])

lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(lst[-1:])
print()

print('Шаг выборки для среза в Python')
txt = '123456789'
print(txt[::2])

txt = '123456789'
res = txt[1:-1:2]
print(res) #2468

lst = ['a', 'b', 'c', 'd', 'e']
print(lst[::3])
print()

print('Срез только с шагом выборки в Python')
txt = '123456789'
print(txt[1::2])

lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[::2])

'''
Составьте кортеж дней недели. 
Получите срез будних дней и срез выходных дней.
'''
DniNedeli = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(DniNedeli[:-2])
print(DniNedeli[-2:])
print()

print('Весь срез в Python')
lst = [1, 2, 3]
lst2 = lst[:]
print(lst2)

num = 4567
num = str(num)
print()

print('Переворот последовательности в Python')
txt = '12345'
print(txt[::-1])

lst = ['c', 'b', 'a']
print(lst[::-1])

txt = '123456789'
print(txt[-2::-2])
print()

print('Удаление элементов с помощью срезов в Python')
lst = [1, 2, 3, 4, 5, 6]
del lst[::2]
print(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
del lst[::2]
print(lst[::-1])