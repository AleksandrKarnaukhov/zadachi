from tokenize import String

print('Многомерные списки в Python')
#Задача 1
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f'{lst[0][1]}' + ' ' + f'{lst[1][0]}' + ' ' + f'{lst[2][1]}')

#Задача 2
lst = [
    ['a', 'b'],
    {'c':1, 'd':2},
    {'e':3, 'f':4}
]
print(f'{lst[1]['c']}' + ' ' + f'{lst[2]['e']}')
print()

print('Трехмерный список в Python')
lst = [
    [
        ['a', 'b'],
        ['c', 'd']
    ],
    [
        ['e', 'f'],
        ['g', 'h']
    ]
]
print(f'{lst[0][0][0]}' + f'{lst[0][1][0]}' + f'{lst[1][0][1]}' + f'{lst[1][1][0]}')

#Задача 2. Посмотрел решение в дипсике. Сомневался, можно ли реализовать трройной цикл.
# мб, автор хотел, чтобы я вручную перебрал... но у меня в голове возник вопрос:
# "А можно ли суммировать с помощью цикла? Их, наверное, будет 3"
lst = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
suma = 0
for i in lst:          # Проходим по двум основным элементам
    for j in i:        # Проходим по внутренним спискам
        for k in j:    # Проходим по числам
            suma += k
print(suma)
print()

print('Перебор многомерных списков в Python')
#Задача 1
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in lst:
    for j in i:
        print(j, end = ' ')
print()

#Задача 2
lst =[
    [2,4,6],
    [3,5,7],
    [9,12,15]
]
z = 0
for i in lst:
    for j in i:
        z += j
print(z)

#Задача 3
lst = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
strk = ''
for i in lst:
    for j in i:
        strk += j
print(strk)
print()

print('Перебор трехмерного списка в Python')
lst = [
	[
		['q', 'w', 'e'],
		['r', 't', 'y'],
		['u', 'i', 'o'],
	],
	[
		['p', 'a', 's'],
		['d', 'f', 'g'],
		['h', 'j', 'k'],
	],
	[
		['l', 'z', 'x'],
		['c', 'v', 'b'],
		['n', 'm', 'q'],
	],
]
for i in lst: # перебор трех массивов внутри lst
    for j in i: # перебор списков внутри отдельного массива
        for k in j: # перебор элементов одного списка в отдельном массиве
            print(k, end = ' ')
print()

#Задача 2
lst = [
	[
		[1, 3],
		[5, 7],
	],
	[
		[2, 4],
		[6, 8],
	],
]
Summa = 0
for i in lst:
    for j in i:
        for k in j:
            Summa += k
print(Summa)
print()

print('Перебор многомерного списка словарей в Python')
#Задача 1
lst = [
	{
		'a': 1,
		'b': 2,
		'c': 3
	},
	{
		'a': 4,
		'b': 5,
		'c': 6
	},
	{
		'a': 7,
		'b': 8,
		'c': 9,
	},
]
summa = 0
for i in lst:
    for j in i.values():
        summa += j
print(summa)

#Задача 2
lst = [
	{
		'a': 1,
		'b': 2,
		'c': 3
	},
	{
		'a': 4,
		'b': 5,
		'c': 6
	},
	{
		'a': 7,
		'b': 8,
		'c': 9,
	},
]
for i in lst:
    for j in i.items():
        print(j)
print()

print('Заполнение многомерных списков Python')
#Задача 1
lst1 = []
for i in range(0, 3):
    lst2 = []
    for j in range(1, 4):
        lst2.append(j)
    lst1.append(lst2)
print(lst1)

#Задача 2
lst1 = []
lst2 = ['a', 'b', 'c']
for i in range(0, 2):
    lst1.append(lst2)
print(lst1)
print()

print('')