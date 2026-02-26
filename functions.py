import math
import random

print('Степень и корень в Python')
#Задача 1
num1 = 5
num2 = 4
print(math.pow(num1, num2))

#Задача 2
dct = {
    2: 4,
    3: 2,
    5: 4
}
for key, value in dct.items():
    print(math.pow(key, value), end = ' ')
print()

#Задача 3
num = 16
print(math.sqrt(num))

#Задача 4
lst = [2, 3, 4]
sumOfnums = 0
for nums in lst:
    sumOfnums += nums
print(math.sqrt(sumOfnums))
print()

print('Функции округления в Python')
#Задача 1
num = 16.456
print(round(num))

#Задача 2
num = 21.167
print(round(num, 2))

#задача 3
num = 3.348
print(math.ceil(num))

#Задача 4
num = 18.565
print(math.floor(num))

#Задача 5
num = 17
print(round(math.sqrt(num), 2))

#Задача 6
num = 17
print(math.ceil(math.sqrt(num)))

#Задача 7
lst = [3.45, 1.54, 5.76]
for elems in lst:
    print(round(elems), end=' ')
print()

#Задача 8
lst1 = [1.514, 4.897, 2.657]
lst2 = []

for nums in lst1:
    lst2.append(math.floor(nums))
print(lst2)

print('Экстремальные числа в Python')
#Задача 1
lst = [2, 4, 6, 8]
print(min(lst))

#Задача 2
tpl = (-1, 2, -6, 3)
print(min(tpl))

#Задача 3
dct = {
    'a': 2,
    'b': 4,
    'c': 5,
    'd': 1
}
print(min(dct.values()))

#Задача 4
num = 123456
str1 = str(num)
listOfstr1 = []
for nums in str1:
    nums = int(nums)
    listOfstr1.append(nums)    
print(f'{min(listOfstr1)} {max(listOfstr1)}')
print()

print('Рандом в Python')
#Задача 1
num1 = 10
num2 = 20
print(random.randint(num1, num2))

#Задача 2
num1 = 5
num2 = 30
print(round(random.uniform(num1, num2)))

#Задача 3
num1 = 1.345
num2 = 14.784
print(random.uniform(num1, num2))

#Задача 4
num1 = -2
num2 = 10
print(random.uniform(num1, num2))

#Задча 5
num1 = 5
num2 = 50
num3 = 4
print(random.randrange(num1, num2, num3))

#Задача 6
lst = [1, 2, 3, 4, 5]
print(random.choice(lst))

#Задача 7
lst = [1, 2, 3, 4, 5]
print(random.sample(lst, 3)) #не понял повторы

#Задача 8
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)

#Задача 9
lst = [1, 1, 1, 2, 2, 3, 3, 4, 5]
set1 = set(lst)
lst1 = list(set1)
print(random.sample(lst1, 3))

#Задача 10
num = 2
random.seed(num) # не понял
print(random.random())

#Задача 11
tpl = (10, 6, 2, 4)
num = random.choice(tpl) #почему тут выводится одно и то же значение?
random.seed(num)
print(random.random())
print()

print('Модули в Python')
#Задача 1
num1 = -8
num2 = -2
sumOfNums = abs(num1) + abs(num2)
print(sumOfNums)

#Задача 2
lst1 = [-3, 4, -1, 6]
lst2 = []
for nums in lst1:
    nums = abs(nums)
    lst2.append(nums)
print(lst2)
print()

print('Математические операции с числами в Python')
#Задача 1
lst = [1, 2, 3, 4, 5]
print(sum(lst))

#Задача 2
st = {2.3, 4, 7.8}
print(math.fsum(st))

#Задача 3
num1 = 2
num2 = 15
randchislo = random.randint(num1, num2) #почему значение одно и то же?
print(math.factorial(randchislo))

#Задача 4
lst = [1, 2, 3, 4, 5]
print(sum(lst)/len(lst))
print()

print('Деление чисел в Python')
#Задача 1
num1 = 10
num2 = 45
print(math.remainder(num2, num1))

#Задача 2
num1 = 12.4
num2 = 30
print(math.fmod(num2, num1))

#Задача 3
num1 = 5
num2 = 3
print(divmod(num1, num2))

#Задача 4
num = 2.34
print(math.modf(num))

#Задача 5
num = 4.8
listofnum = list(math.modf(num))
print(listofnum)
print()

print('Регистр символов в Python')
#Задача 1
txt = 'ABCDE'
print(txt.lower())

#Задача 2
txt = 'abcde'
print(txt.upper())

#Задача 3
txt = 'abcde'
print(txt.capitalize())

#Задача 4
txt = 'word1 word2 word3'
print(txt.title())

#Задача 5
txt = 'ABC def'
print(txt.swapcase())

#Задача 6
lst = ['ab', 'Cd', 'eF']
lst2 = []
for el in lst:
    lst2.append(el.capitalize())
print(lst2)

#Задача 7
emails = {
    'Sanya': 'aBEma',
    'Max': 'DoteR'
}
for value in emails.values():
    print(value.lower(), end=' ')
print()
print()

print('Разбиения строк в в Python')
#Задача 1
txt = 'a/b/c/d'
print(txt.split('/'))

#Задача 2
txt = 'a.b.c.d'
print(txt.rsplit('.', 1))

#Задача 3
txt = 'ab%cd%'
print(txt.partition('%'))

#Задача 4, 5
txt = '2025-12-31'
print(txt.rpartition('-'))

#Задача 6
lst = ['a', 'b', 'c', 'd']
text = ''.join(lst)
print(text)

#Задача 7
lst = ['2025', '31', '12']
txt = '/'.join(lst)
print(txt)

#Задача 8
lst = [1, 2, 3]
lst2 = []
for el in lst:
    lst2.append(str(el))
txt = ''.join(lst2)
print(txt)
print()

print('Форматирование строк в в Python')
#Задача 1 - хз как решать

#Задача 2, 3, 4, 5
txt = ' abcde '
print(txt.strip())

txt = ' abcde '
print(txt.lstrip())

txt = ' abcde '
print(txt.rstrip())

#Задача 6
txt = 'abc {}'
num = 12
print(txt.format(num))

#Задача 7
text = 'Саня {}'
print(text.format(24))

#Задача 8
txt = ''
num = 6
print(txt.zfill(num))

#Задача 9
txt = 'abcde'
print(txt.ljust(len(txt)+3, '1'))

#Задача 10
txt = '12345'
print(txt.rjust(len(txt)+2, 'a'))
print()

print('Поиск по строкам в Python')
#Задача 1
txt = 'abcdef'
print(txt.startswith('ac'))

#Задача 2
lst = ['12', '13', '14', '15']
for elems in lst:
    print(elems.startswith('1'), end=' ')
print()

#Задача 3
num = 123456
num = str(num)
print(num.endswith('6'))

#Задача 4
txt = 'abcdef'
print(txt.index('c'))

#Задача 5
txt = 'ab1cd1ef'
print(txt.index('c', 3, 7))

#Задача 6
txt = '123453637'
print(txt.rindex('3'))

#Задача 7
txt = '2025.12.31'
print(txt.rindex('2'))

#Задача 8
num = 24536589
num = str(num)
print(num.count('5'))

#Задача 9
lst = ['abc', 'cde', 'cbb', 'aeb']
for elems in lst:
    print(elems.count('b'), end=' ')
print()

#Задача 10
txt = 'http1://code.mu'
print(txt.replace('1', 's'))

#Задача 11
txt = 'a.bc.d.ef'
print(txt.replace('.', ' '))
print()

print('Проверка строки в Python')
#Задача 1
txt = 'Abcde'
print(txt.istitle())

#Задача 2
lst = ['User1', 'User2', 'user3', 'User4']
for el in lst:
    print(el.istitle(), end=' ')
print()

#Задача 3
txt = 'ABCDE'
print(txt.isupper())

#Задача 4
txt = 'abcde'
print(txt.islower())

#Задача 5
txt = 'abcde'
print(txt.isalpha())

#Задача 6
txt = '12345'
print(txt.isdigit())

#Задача 7
txt = 'Ⅷ'
print(txt.isnumeric())

#Задача 8
txt = '12345abc'
print(txt.isalnum())

#Задача 9
txt = 'a1b2c3d '
print(txt.isalnum())

#Задача 10
txt = ' '
print(txt.isspace())

#Задача 11
lst = ['a', 'b', ' ', 'c', '']
for elems in lst:
    print(elems.isspace(), end=' ')
