from calendar import month

print('Операторы больше и меньше в Python')
#Задача 1
tst = 5
if tst > 10:
    print('ok')
else:
    print('no')

#Задача 2
if tst < 10:
    print('correct')

#Задача 3
if tst >= 5:
    print('nice')

#Задача 4
if tst <= -5:
    print('slayer')
else:
    print('()')

#Задача 6
age = 24
if age >= 18:
    print('You have access to the site')
else:
    print('You do not have access to the site')

print()

print('Проверка на равенство в Python')
#Задача 1
tst = 25
if tst == 10:
    print('25 = 10')

#Задача 2
tst = '123'
if tst == 123:
	print('+++')
else:
	print('---') #---

#Задача 3
tst = ['a', 'b', 'c', 'd']
if len(tst) == 5:
	print('+++')
else:
	print('---') #---

print()

print('Проверка на неравенство в Python')
#Задача 1
tst = -4
if tst != 4:
    print('ne')

#Задача 2
tst = 123
if tst != 123:
	print('+++')
else:
	print('---') #---

#Задача 3
tst = ['a', 'b', 'c']
if tst[1] != 'c':
	print('+++')
else:
	print('---') #+++

#Задача 4
tst1 = [3, 4, 5, 6]
tst2 = list('3456')
if tst1 != tst2:
	print('+++')
else:
	print('---') #+++

print()

print('Логическое И в Python')
#Задача 1
tst = -3
if tst > 0 and tst < 5:
    print('+++')
else:
    print('8==D')

#Задача 2
tst = 21
if tst > 10 and tst <= 20:
    print('sobaka')
else:
    print('jaba')

#Задача 3
tst1 = 6
tst2 = 10
if tst1 < 8 and tst2 >= 10:
    print('mars')
else:
    print('twix')

#Задача 4
tst1 = 'abcde'
tst2 = list(tst1)
if len(tst1) >= 5 and len(tst2) < 8:
	print('+++')
else:
	print('---') #+++

print()

print('Логическое ИЛИ в Python')
#Задача 1
tst1 = -1
tst2 = 4
if tst1 <= 1 or tst2 >= 3:
    print('watermelon')
else:
    print('orange')
#Остальные зхадачи не решал, т.к. нафиг надо

print()

print('Логическое НЕТ в Python')
#Задача 1
tst = 15
if tst > 20 and not tst < 10:
	print('+++')
else:
	print('---') #---

#Задача 2
tst1 = -8
tst2 = 10
if tst1 > -10 and not tst2 < 10:
	print('+++')
else:
	print('---') #+++

print()

#Скип - Приоритет операций сравнения в Python
#Скип - Группировка условий в Python

print('Двойные сравнения в Python')
#Задача 1
tst = 15
if 10 < tst < 20:
    print('jaba')

#Задача 2
tst = -5
if 0 > tst > -10 or -8 < tst < 30:
    print('abema')

#Задача 3
tst = ['a', 'b', 'c', 'd', 'e']
if 6 > len(tst) > 0:
    print('author')

print()

print('Проверка наличия в Python')
#Задача 1
tst = 'x'
lst = ['x', 'y', 'z', 'w']
if tst in lst:
    print('cock')

#Задача 2
tst = '1'
st = {1, 2, 3, 4, 5}
if tst not in st:
    print('jaba')

#Задача 3
tst = '3'
txt = '123456'
if tst in txt:
    print('uzor')

print()

print('Проверка на специальные значения в Python')
#Задача 1
tst = 10
if tst is None:
    print('tarelka')
else:
    print('lojka')

#Задача 2
tst = 'abc'
if tst is not None:
    print('tarelka')
else:
    print('lojka')

print()

#Скип - Сокращенный if в конструкции if-else

print('Конструкция elif в Python')
#Задача 1
tst1 = 5
tst2 = 8
if tst1 > tst2:
    print('5 больше 8')
elif tst1 < tst2:
    print('5 меньше 8')

#Задача 2
age = 24
if 18 > age > 10:
    print('a')
elif 18 < age < 60:
    print('b')
else:
    print('c')

#Задача 3
day = 11
if 1 < day < 11:
    print('Первая декада')
elif 10 < day < 21:
    print('Вторая декада')
else:
    print('Третья декада')

print()

print('Вложенные if в Python')
#Задача 1
month = 12
if month in range(1, 12):
    if month != 1 and month != 2 and month != 12:
        if 2 < month < 6:
            print('Весна')
        elif 5 < month < 9:
            print('Лето')
        else:
            print('Осень')
    else:
        print('Зима')
else:
    print('число вне диапозона')

#Задача 2
num = 98
sum = 0
if num in range(10, 99):
    num = str(num)
    sum = int(num[0]) + int(num[1])
    if sum <= 9:
        print(f'сумма цифр однозначная = {sum}')
    else:
        print(f'сумма цифр двухзначная = {sum}')
else:
    print('число вне диапозона')

print()

print('Конструкция match-case в Python')
#Задача 1
num = 1
match num:
    case 1:
        print('Зима')
    case 2:
        print('Весна')
    case 3:
        print('Лето')
    case 4:
        print('Осень')

#Задача 2
num = 7
match num:
    case 12 | 1 | 2:
        print('Зима')
    case 3 | 4 | 5:
        print('Весна')
    case 6 | 7 | 8:
        print('Лето')
    case 9 | 10 | 11:
        print('Осень')

print()

print('Тернарный оператор в Python')
#Задача 1
tst = 12
print('+++' if tst > 0 else '---')

#Задача 2
tst = 'abcde'
print('+++' if 'a' in tst else '---')

print()

print('Проверка типа объекта в Python')
z = (1, 2, 3)
if isinstance(z, int):
    print('число')
if isinstance(z, float):
    print('число с точкой')
if isinstance(z, str):
    print('строка')
if isinstance(z, set):
    print('множество')
if isinstance(z, tuple):
    print('кортеж')
if isinstance(z, list):
    print('список')

print()

print('Практикум на if-else в Python')
#Задача 1
num = 2
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

#Задача 2
txt = 'abcdef'
if 'a' in txt:
    txt = txt.replace('a', '!')
    print(txt)

#Задача 3
MAIL = 'abema@mail.ru'
if '@' in MAIL:
    print(txt)
else:
    print('повторите попытку') #мб, через инпут надо делать, но мне пофиг

#Задача 4
name = "Alex"
if len(name) < 3:
    print('имя слишком короткое')
elif len(name) in range(3,20):
    print('normalno')
else:
    print('сократи имя')

#Задача 5
password = '1234561232342342'
if len(password) == 0:
    print('ты еблан?')
elif len(password) in range(6, 14):
    print('ok')
else:
    print('not ok')

#Задача 6
tst = 'abcdef'
print('string is too long' if len(tst) > 20 else 'string is too short')