from os import remove

print('Словари в Python')
dct = {
    'z' : 1,
    'x' : 2,
    'c' : 3
}
print(dct)

CB = {
    2 : 'ab',
    4 : 'cd',
    6 : 'ef'
}
print(CB)

bio = {
    'surname' : 'Карнаухов',
    'name' : 'Саня',
    'date' : '10.02.2002'
}
print(bio)

mesyac = {
    1 : 'January',
    2 : 'February',
    3 : 'Mart',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December'
}
print(mesyac)
print()

print('Альтернативный способ создания словаря в Python')
dct = dict(a=1, b=2, c=3)
print(dct)

''' ошибка
dict('1'='a', '2'='b', '3'='c')
print('dict')
'''

dict(a='12', b='34', c='56')
print(dct)

''' ошибка
dct = dict(0='abc', 1='def')
print(dct)
'''
print()

print('Значение элемента словаря в Python')
dct = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
print(dct['x'])
print(dct['y'])
print(dct['z'])

dct = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(dct['b'])

dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
key = 'x'
print(dct[key])

dct = {
	'a': 5,
	'b': 10,
	'c': 15
}
print(dct['a'] + dct['b'] + dct['c']) #по-отдельности не стал выводить занчения ключей.

dct = {
	1: 'a',
	2: 'b',
	3: 'c'
}
print(dct[1] + dct[2] + dct[3])
print()

print('Изменение значения элемента словаря в Python')
dct = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
dct['x'] += 1
print(dct)

dct = {
    'surn' : 'smit',
    'name' : 'john'
}
dct['surn'] = 'Гиперборейский'
dct['name'] = 'shizopunk'
print(dct['surn'] + ' ' + dct['name'])
print()

print('Добавление элемента в словарь в Python')
dct = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
dct['a'] = 4
dct['b'] = 5
dct['c'] = 6
print(dct)
print()

print('Длина словаря в Python')
dct = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
print(len(dct))

dct1 = {
	'a': 12,
	'b': 34,
	'c': 56,
	'd': 78,
	'e': 90
}
dct2 = {
    'dct1' : len(dct1)
}
print(dct2)
print()

print('Объединение словарей в Python')
dct1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
dct2 = {
    'x' : 4,
    'y' : 5,
    'z' : 6
}
dct1.update(dct2)
print(dct1)

dct1 = {
	'3': 'c',
	'4': 'd',
	'5': 'e'
}

dct2 = {
	'1': 'a',
	'2': 'b'
}
dct2.update(dct1)
print(dct2)

dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct2 = {
	'x': 4,
	'y': 5,
	'z': 6
}
dct1.update(dct2)
print(dct1)

dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct2 = {
	'd': 4,
	'e': 5,
	'f': 6
}

dct3 = {
	'j': 7,
	'h': 8,
	'i': 9
}
dct2.update(dct3)
dct1.update(dct2)
print(dct1)
print()

print('Объединение словарей с одинаковыми элементами в Python')
dct1 = {
	'z': 2,
	'w': 8,
	'f': 10
}

dct2 = {
	'x': 4,
	'y': 5,
	'z': 6
}
dct1.update(dct2)
print(dct1) #'z':6 'w':8 'f':10 'x':4 'y':5

dct1 = {
	2: 'a',
	4: 'b',
	6: 'c'
}

dct2 = {
	1: 'd',
	3: 'e',
	4: 'f',
	7: 'j'
}

dct2.update(dct1)
print(dct2) #1,3 - без изм; 4: 'b'; остальное без изменений
print()

print('Удаление элементов из словаря по ключу в Python')
dct = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
del dct['x']
print(dct)

dct = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd',
	5: 'e'
}
del dct[2]
del dct[4]
print(dct)
print()

print('Извлечение элемента по ключу в Python')
dct = {
	'x' : 1,
	'y' : 2,
	'z' : 3
}
print(dct.pop('x'))

''' ошибка, т.к. в попе указано значение а не ключ
dct = {
	1: '1',
	2: '2',
	3: '3'
}
print(dct.pop('2'))
'''

dct = {
	'surn': 'smith',
	'name': 'john',
	'age': 30
}
dct.pop('surn')
print(dct) #уберет фамилию
print()

print('Извлечение последнего элемента в Python')
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
tpl = dct.popitem()
print(tpl)

dct = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd',
	5: 'e'
}
kort1 = dct.popitem()
lst = []
lst.append(kort1[0])

kort2 = dct.popitem()
lst.append(kort2[0])

kort3 = dct.popitem()
lst.append(kort3[0])

kort4 = dct.popitem()
lst.append(kort4[0])

kort5 = dct.popitem()
lst.append(kort5[0])
print(lst)
print()

print('Удаление всех элементов из словаря в Python')
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
dct.clear()
print(dct)

dct = {
	1: 'text1',
	2: 'text2',
	3: 'text3'
}
dct.clear()
dct[4] = 'text4'
print(dct) #{4 : 'text4'}
print()

print('Наличие элемента в словаре в Python')
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print('w' in dct) #False

dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
print('x' in dct) #False

dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
print('x' not in dct) #True

dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
print(3 in dct) #True
print()

print('Опциональное получение элемента из словаря в Python')
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
print(dct.get(4)) #'w'

dct = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd'
}
print(dct.get('3')) #none

dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct.get('w', '!'))
print()

print('Преобразование значений словаря в список в Python')
dct = {
	1: 'ab',
	2: 'cd',
	3: 'ef'
}
print(list(dct))

dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
lst = list(dct)
lst.reverse()
print(lst)
print()

print('Получение всех ключей из словаря в Python')
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct.keys())

dct = {
	2: 'ab',
	4: 'cd',
	6: 'ef'
}
lst = list(dct.keys())
print(lst[0] * lst[1] * lst[2])

dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
lst = list(dct.keys())
lst = lst[::-1]
print(lst)
print()

print('Получение всех значений из словаря в Python')
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct.values())

dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
print(dct.values())

dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(list(dct.values()))

dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}
dct2 = {
	1: 'a',
	2: 'b',
	3: 'c'
}
dct1.update(dct2)
print(list(dct1.values()))
print()

print('Получение пары ключ-значение из словаря в Python')
dct = {
	'x': 3,
	'y': 2,
	'z': 1
}
print(dct.items())

dct = {
	'a': [2, 4],
	'b': [3, 5]
}
print(dct.items())

dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
print(list(dct.items()))

dct = {
	'a': 12,
	'b': 34,
	'c': 56
}
sp = list(dct.items())
lst = [sp[0][0], sp[0][1], sp[1][0], sp[1][1], sp[2][0], sp[2][1]]
print(lst)
print()

print('Преобразование в словарь в Python')
tst = [[1, 'ab'], [2, 'cd'], [3, 'ef']]
dct = dict(tst)
print(dct) #{1: 'ab' и т.д.}

tst = [('x', 2), ('y', 4), ('z', 6)]
dct = dict(tst)
print(dct)

''' ошибку
tst = ['a', 'b', 'c', 'd']
dct = dict(tst)
print(dct)
'''

tst = ('a', 1), ('b', 2), ('c', 3)
dct = dict(tst)
print(dct)
print(type(tst))
print()

print('Отработка изученного материала на работу со словарями в Python')
#задача 1
dct = {
	'x': '1',
	'y': '2',
	'z': '3'
}
znach = list(dct.values())
print(int(znach[0]) ** 2 + int(znach[1]) ** 2 + int(znach[2]) ** 2)

#задача 2
dct1 = {
	'1': 12,
	'2': 24,
	'3': 36
}
dct2 = {
	'a': '3',
	'b': '6',
	'c': '9'
}
znach1 = list(dct1.values())
sum1 = int(znach1[0]) + int(znach1[1]) + int(znach1[2])

znach2 = list(dct2.values())
sum2 = int(znach2[0]) + int(znach2[1]) + int(znach2[2])
print(sum1 + sum2)

#задача 4
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
spisok = list(dct.values())
spisok[0] = str(spisok[0])
spisok[1] = str(spisok[1])
spisok[2] = str(spisok[2])
print(spisok[0] + spisok[1] + spisok[2])

#задача 5
dct = {
	'a': 7,
	'b': 6,
	'c': 5
}
spisok = list(dct.values())
spisok[0] = str(spisok[0])
spisok[1] = str(spisok[1])
spisok[2] = str(spisok[2])
result = "/".join(spisok)
print(result[::-1])

#задача 6
dct = {
	'y': 2025,
	'm': 12,
	'd': 31
}
spisok = list(dct.values())
spisok[0] = str(spisok[0])
spisok[1] = str(spisok[1])
spisok[2] = str(spisok[2])
result = "-".join(spisok)
print(result)