print('Тема: Множества в Python')
tst = {}
print(type(tst)) #словарь

tst = set()
print(type(tst)) #множество

tst = {'x', 'y', 'z'}
print(type(tst)) #множество

tst = {'a': 1, 'b': 2, 'c': 3}
print(type(tst)) #словарь
print()

print('Тема: Элемент множества в Python')
'''
st = {'1', '2', '3'}
print(st['2']) #ошибка

st = {3, 4, 5}
print(st[0]) #ошибка
'''
print()

print('Тема: Повторяющиеся элементы в множестве в Python')
st = {'ab', 'bc', 'cd', 'bc'}
print(st) #{'ab', 'bc', 'cd'}

st = {'12', '34', '56', 34}
print(st) #{'12', '34', '56', 34}
print()

print('Тема: Длина множества в Python')
st = {'x', 1, 'y', 2, 'z', 3, 'w'}
print(len(st))

st = {1, 2, 3, 4, 2, 1}
print(len(st))
print()

print('Ткма: Добавление элемента в множество в Python')
st = {1, 2, 3}
st.add(10)
print(st)

txt1 = 'xyz'
txt2 = 'xzy'
txt3 = 'xyz'
st.add('xyz')
st.add('xzy')
st.add('xyz')
print(st)
print()

print('Тема: Добавление нескольких элементов в множество в Python')
st = {'x', 'y', 'z', 'w'}
st.update('abxcz')
print(st)

st = {1, 2, 3}
lst = [3, 4, 5, 6]
st.update(lst)
print(st)

st = {'12', '34', '56'}
tlp = (2, 4, 6)
st.update(tlp)
print(st) #2, 4, 6, 12, 34, 56
print()

print('Тема: Объединение множеств в Python')
st1 = {'a', 'b', 'c', 'd', 'e'}
st2 = {'d', 'e', 'f', 'g', 'h'}
st1.update(st2)
print(st1)

st1 = {'2', '4', '6'}
st2 = {7, 8, 9}
st3 = {'1', '3', '4'}
st1.update(st2, st3)
print(st1)

st1 = {1, 2, 3}
st2 = {'a', 'b', 'c'}
st3 = {4, 5, 6}
st4 = {'d', 'e', 'f'}
st1 = st1 | st3
st2 = st2 | st4
print(st1)
print(st2)
print()

print('Тема: Удаление элемента из множества в Python')
st = {1, 2, 3, 4, 5}
st.remove(3)
print(st)

'''
st = {'12', 1, '34', 2, '56'}
st.remove('1')
print(st) #ошибка
'''

st = {1, 7, '2', 14, 5, 2}
st.remove(2)
print(st) #удалит интовую двойку
print()

print('Тема: Удаление присутствующего в множестве элемента в Python')
st = {'x', 'y', 'z'}
st.discard('y')
print(st)

st = {1, 2, 3, 4, 5}
st.discard(2)
st.discard(4)
print(st)

st = {'ab', 'cd', 'ef'}
st.discard('b')
print(st) #{'ab', 'cd', 'ef'}
print()

print('Тема: Извлечение элемента из множества в Python')
st = {1, 2, 3, 4, 5}
st.pop()
print(st)

st = {'a1', 'b2', 'c3', 'd4'}
st.pop()
st.pop()
print(st)
print()

print('Тема: Удаление всех элементов из множества в Python')
st = {1, 2, 3, 4, 5}
st.clear()
print(st)

st.update([1, 2, 3])
print(st)
print()

print('Тема: Наличие элемента в множестве в Python')
st = {1, 2, 3, 4, 5}
num = 3
print(num in st)

st1 = {'1', '2', '3'}
st2 = {'4', '5', 3}
print('3' in st1 & st2) #False

st = {'ab', 'bc', 'cd'}
txt = 'bc'
print(txt not in st) #False

st = {'x', 'y', 'z', 'w'}
txt = 'yz'
print(txt not in st) #True
print()

print('Тема: Наличие множества в последовательности в Python')
st = {'1', '2', '3', '4', '5', '6'}
txt = '123456'
print(st.issubset(txt))

st = {'ab', 'cd', 'ef'}
tlp = ('ab', 'cd', 'ef')
print(st.issubset(tlp))

st1 = {1, 2, 3, 4, 5}
st2 = {1, 2, 3}
print(st2.issubset(st1))
print()

print('Тема: Сравнение множеств в Python')
st1 = {'a', 'f', 'e', 'b'}
st2 = {'f', 'a', 'b', 'e'}
print(st1 == st2)

st1 = {'1', '4', '2', '3'}
st2 = {'2', '3', '4', 1}
print(st1 == st2) #False
print()

print('Тема: Общие элементы нескольких множеств в Python')
st1 = {'12', '6', '2'}
st2 = {'6', '10', '3', '2'}
print(st1.intersection(st2))

st1 = {1, 2, 3, 4}
st2 = {1, 2, 4, 5}
st3 = {1, 2, 5, 7}
print(st1 & st2 & st3)
print()

print('Тема: Разные элементы нескольких множеств в Python')
st1 = {'a', 'b', 'c', 'd', 'e'}
st2 = {'d', 'e', 'f', 'g', 'h'}
print(st1.symmetric_difference(st2))

st1 = {2, 4, 8, 10}
st2 = {1, 8, 3, 2}
st3 = {4, 7, 3, 1}
st4 = st1 ^ st2
print(st4)
st4 = st4 ^ st3
print(st4)
print()

print('Тема: Разность множеств в Python')
st1 = {'1', '3', '5'}
st2 = {'6', '8', '1', '3'}
print(st2.difference(st1))

st1 = {'a', 'b', 'c', 'd', 'e'}
st2 = {'d', 'e', 'f', 'g', 'h'}
print(st1 - st2)

st1 = {1, 2, 4, 5}
st2 = {1, 2, 3, 6}
st3 = {1, 2}
st4 = st1 - st3
st5 = st2 - st3
st4.update(st5)
print(st4)

st1 = {1, 3, 6, 8}
st2 = {5, 8, 10, 2}
st3 = {12, 7, 3, 1}
st4 = st1 - st2
print(st4 & st3)
print()

print('Тема: Сложные операции со множествами в Python')
st1 = {1, 3, 6, 8}
st2 = {5, 8, 4, 2}
st3 = {4, 7, 3, 1}
print((st1 | st3) & st3)

st1 = {4, 2, 6, 10}
st2 = {1, 6, 3, 2}
st3 = {5, 8}
st4 = {6, 3, 1}
print((st1 - st2) & (st3 | st4))
print()

print('Тема: Преобразование в множество в Python')
txt1 = '1234'
txt2 = '5678'
print(set(txt1 + txt2))

tlp = ('a', 'b', 'c', 'd')
print(set(tlp))

dct = {
	1: 'ab',
	2: 'cd',
	3: 'ef',
	4: 'jh'
}
kl = dct.keys()
zn = dct.values()
print(set(kl))
print(set(zn))
print()

print('Тема: Отработка изученного материала на работу с множествами в Python')
#Задание 1
st1 = {'x', '1', 'y', '2', 'z'}
st2 = {1, 2, 3, 4, 5, 6}

print(len(st1))
print(len(st2))
print()

#Задание 2
num1 = 12345
num2 = 12321

mn1 = set(str(num1))
mn2 = str(num2)

print(mn1.issubset(mn2))
print()

#Задание 3
tst1 = 34
tst2 = [1, 2, 5]
tst3 = (6, 7, 8)

tst1 = [tst1]
SumOfList = tst2 + tst1

mnoj1 = set(SumOfList)
mnoj2 = set(tst3)

print(mnoj1 | mnoj2)
print()

#Задание 4
st = {'18', '24', '34', '47', '81', '63'}
tst1 = '34'
tst2 = ('81', '12', '46')

tst1 = set(tst1)
tst2 = set(tst2)

print(st <= tst1)
print(st <= tst2)
print()

#Задание 5
num1 = 12345
num2 = 45123

mn1 = set(str(num1))
mn2 = set(str(num2))

print(mn1 == mn2)
print()

#Задание 6
num1 = 12345
num2 = 45678

mn1 = set(str(num1))
mn2 = set(str(num2))

SameValues = mn1 & mn2
SameValues = list(SameValues)

chislo = int(SameValues[0]) + int(SameValues[1])
print(chislo)
print()

#Задание 7
st1 = {'ab', 'b', 'ce', 'de', 'd'}
st2 = {'ef', 'd', 'ab', 'bc'}
st3 = {'a', 'g', 'b', 'c'}

print((st1 & st2) | st3)








