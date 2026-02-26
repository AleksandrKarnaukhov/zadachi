print('Цикл for в Python')
#Задача 1
tst = ['1', '2', '3', '4', '5']
for el in tst:
    print(el, end=' ')
print()

#Задача 2
tst = 1, 2, 3, 4, 5
for el in tst:
    print(el, end=' ')
print()

#Задача 3
tst = {'a', 'b', 'c', 'd', 'e'}
for el in tst:
    print(el, end=' ')
print()

#Задача 4
tst = 'abcde'
for el in tst:
    print(el, end=' ')
print()

#Задача 5
tst = 12345
tst = str(tst)
for el in tst:
    print(el, end=' ')
print()

#Задача 6
tst = [1, 2, 3, 4, 5]
for el in tst:
    print(el + 2, end=' ')
    
print()

print('Накопление результата в цикле for Python')
#Задача 1
tst = [1, 2, 3, 4, 5]
SumKv = 0
for el in tst:
    SumKv += el ** 2
print(SumKv)

#Задача 2
tst = ['a', 'b', 'c', 'd', 'e']
string = ''
for el in tst:
    string += el
print(string)

#Задача 3
tst = [1, 2, 3, 4, 5]
SumOfEl = 0
for el in tst:
    SumOfEl += el
print(SumOfEl)

print()

print('Цикл for и условие if в Python')
#Задача 1
tst = {-2, 1, 3, -5, 4, -8}
for el in tst:
    if el > 0:
        print(el, end=' ')

#Задача 2
tst = [7, 1, 2, 5, 3, 9]
lst = []
for el in tst:
    if 2 < el < 5:
        lst.append(el)
print(lst)

#Задача 3
tst = (1, 2, 3, 4, 5, 6, 7)
SumChet = 0
for el in tst:
    if el % 2 == 0:
        SumChet += el
print(SumChet)

#Задача 4
tst = 1234567
newlist = []
tst = str(tst)
for el in tst:
    el = int(el)
    if el % 2 != 0:
        newlist.append(el)
print(newlist)

print()

print('Инструкция break в Python')
#Задача 1
tst = {1, 3, 6, 7, -9, 12}
for el in tst:
    print(el, end=' ')
    if el < 0:
        break

#Задача 2
tst = [7, 1, 2, 5, 0, 3, 9]
SumOfEl = 0
for el in tst:
    SumOfEl += el
    if el == 0:
        break
print(SumOfEl)

#Задача 3
tst = 897654
new_tst = str(tst)
lst = []
for el in new_tst:
    lst.append(el)
    if el == '6':
        break
print(lst)

print()

print('Инструкция continue в Python')
#Задача 1
tst = {'a', 'b', 'c', 'd', 'e'}
for el in tst:
    if el == 'd':
        continue
    print(el, end=' ')
print()

#Задача 2
tst = [6, 3, -2, 8, -4, 9]
for el in tst:
    if el < 0:
        continue
    print(el, end=' ')
print()

#Задача 3
tst = ['a', 'b', 'c', 'd', 'e']
for el in tst:
    if el == 'b':
        continue
    print(el, end=' ')

print()

print('Получение элементов и их индексов в Python')
#Задача 1
tst = [8, 6, -4, 2, -1]
for key, value in enumerate(tst):
    if value < 0:
        break
    print(key, end =' ')
    print(value)

print()

#Задача 2
tst = ['a', 'b', 'c', 'd', 'e']
for key, value in enumerate(tst, start = 1):
    print(value, end='')
    print(key)

print()

#Задача 3
tst = [1, 2, 3, 4, 5]
for key, value in enumerate(tst):
    if key == 0:
        print('ноль не является ни четным, ни нечетным')#поэтому value не возвожу в степень
    elif key % 2 == 0:
        print(value ** 2, end =' ')
    else:
        print(value ** 3, end =' ')
print()

print()

print('Ключи словаря через for в Python')
#Задача 1
tst = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5
}
for key in tst:
    print(key, end =' ')

print()

#Задача 2
tst = {
	2: 'a',
	4: 'b',
	6: 'c',
	8: 'd'
}
for key in tst:
    if key == 8:
        continue
    print(key, end =" ")

print()

#Задача 3
tst = {
	'1': 'a',
	'2': 'b',
	'3': 'c',
	'4': 'd'
}
lst = [ ]

for key in tst:
    if key == '1':
        continue
    lst.append(key)
    tpl = tuple(lst)
print(tpl)

print()

print('Значения словаря через for в Python')
#Задача 3
tst = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5
}
for i in tst:
    print(tst[i])

print()

#Задача 2
tst = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5
}
sum = 0
for value in tst.values():
    sum += value
print(sum)

print()

#Задача 3
tst = {
	'1': 'a',
	'2': 'b',
	'3': 'c',
	'4': 'd'
}
for i in tst.values():
    print(i, end ='')
print()

print()

print('Пара ключ-значение словаря через for в Python')
#Задача 1
dct = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5
}
for i in dct.items():
    print(i, end = ' ')

print()

#Задача 2
dct = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}
for i in dct.items():
    print(i)
    
print()

print('Пары индекс-элемент словаря в Python')
#Задача 1
tst = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5
}
for i in enumerate(dct):
    print(i, end =' ')

print()

#Задача 2
tst = {
	'1': 11,
	'2': 12,
	'3': 13,
	'4': 14
}
for k in enumerate(tst):
    print(k, end='')

print()

#Задача 3
tst = {
	'x': 10,
	'y': 20,
	'z': 30
}
for k in enumerate(tst):
    print(k, end='')

print()
print()

print('Генерация чисел через for в Python')
#Задача 1
for i in range(1, 10):
    print(i, end=' ')
print()

#Задача 2
for j in range(20, 10):
    print(j)#Ничего не выведет

#Задача 3
lst = []
for i in range(1, 6):
    lst.append(i)
print(lst)

#Задача 4
sum = 0
for i in range(1, 101):
   sum += i
print(sum)

print()

print('Генерация чисел с шагом через for в Python')
#Задача 1
for i in range(2, 101, 2):
    print(i, end=' ')
print()

#Задача 2. Автор, наверное, еблан и имел ввиду от 10 до -10
for i in range(10, -11, -1):
   print(i, end=' ') 
print()

#Задача 3
for i in range(2, 21, 3):
    print(i, end=' ')
print()

print()

print('Одновременный перебор последовательностей в Python')
#Задача 1

tst1 = [1, 3, 5]
tst2 = [2, 4, 6]
for el in zip(tst1, tst2):
    print(el)

print()

#Задача 2
tst1 = ['a', 'b', 'c']
tst2 = ['d', 'e', 'f']
tst3 = []
for el in zip(tst1, tst2):
    tst3.append(el[0])
    tst3.append(el[1])
print(tst3)

#Задача 3
tst1 = [11, 12, 13, 14]
tst2 = [21, 22, 23, 24]
tst3 = [31, 32, 33, 34]
summa = 0
tst4 = []

for el in zip(tst1, tst2, tst3):
    summa = el[0] + el[1] + el[2]
    tst4.append(summa)
print(tst4)
    
print()

print('Цикл while в Python')
#Задача 1
num = 0
while num < 10:
    num += 1
    print(num, end = ' ')
print()

#Задача 2
num = 100
while 0 < num <= 100:
    print(num, end = ' ')
    num -= 1
print()
print()

#Задача 3
num = 1
while 0 < num < 100:
    print(num, end = ' ')
    num +=2
print()

print()

print('Цикл while без счетчика в Python')
#Задача 1
num = 100
while num > 20:
    num = num // 3
    print(num, end = ' ')
print()

#Задача 2
num = 1
while num < 20:
    num = num * 2.5
    print(num, end = ' ')
print()

print()

print('Условие if в цикле while в Python')
#Задача 1
num = 125
while True:
    num = num // 2
    if num < 10:
        break
print(num)

#Задача 2
num = 29
el = 0
lst = []
while True:
    el += 1
    if el in range(1, num + 1) and num % el == 0:
        lst.append(el)
    elif el not in range(1, num + 1):
        break
print(lst)

print()

print('Работа с флагами в Python')
#Задача 1
list1 = [1, 2, 3, 4, 5, -10]
f = True
for el in list1:
    if el < 0:
        f = False
print(f)

#Задача 2
num = 7
el = 0
f = False
for el in range(2, num):
    if num % el == 0:
      break  
    else:
        f = True
print(f)

print()

print('Перехват выхода из цикла в Python')
#Задача 1
list1 = [100, -14, 9114, -12]
for i in list1:
    if i < 0:
        print('-')
        break
else:
    print('+')
print()

#Задача 2
tst = 'abcdef'
for i in tst:
    if i == 'd':
        print('+')
        break
else:
    print('-')
print()

print('Практикум на циклы в Python')
#Задача 1
tst = {
	'1': 'a',
	'2': 'b',
	'3': 'c',
	'4': 'd'
}
list1 = []
for key, value in  tst.items():
    list1.append(key)
    list1.append(value)
print(list1)
print()

#Задача 2
str1 = ''
for num in range(1, 20):
    if num % 2 == 0:
        num = str(num)
        str1 += num
print(str1)
print()

#Задача 3
for num in range(1, 100):
    if num % 2 != 0:
        print(num, end = ' ')
print()
print()

#Задача 4
list2 = []
while len(list2) < 10:
    list2.append('x')
print(list2)
print(len(list2))
print()

#Задача 5
mnoj = set()
str2 = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0, 10):
    mnoj.add(str2[i])
print(mnoj)
print()

#Задача 6
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in tpl:
    if 5 < i < 10:
        print(i, end = ' ')
print()

#Задача 7
stroka = 'cklbnvzlxfnclonolzbgn'
for i in stroka:
    if 'c' in stroka:
        print(True)
    break
print()

#Задача 8
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summa = 0
znam = len(list1)
for i in list1:
    summa += i
print(summa/znam)


#Задача 9
list2 = [-3, 2, 3, 5, 6, -1, 0]
for i in list2:
    print(i)
    if i > 0:
        break    
print()

#Задача 10
dict1 = {
    1: ('alex', 'karnaukhov', 24),
    2: ('vika', 'kopasova', 22)
}
for i in dict1.items():
    print(i)
print()

#Задача 11
for j in dict1.values():
    print(j[0].title())
print()

#Доп. задание
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Prostie = []
Sostavnie = []

