wesgbSEDRGSEGSEGVsegprint('Создание кортежа в Python')
tst = (12, 34, 45)
print(type(tst)) #кортеж

tst = [1, 2, 3]
print(type(tst)) #список

tst = ([1, 2, 3], True, 'a', 'b')
print(type(tst)) #кортеж
print()

print('Альтернативный способ создания кортежа в Python')
tst = '12345'
tst = tuple(tst)
print(tst)

txt = '12345'
tpl = tuple(txt)
print(tpl)

tst = 98765
tst = str(tst)
print(tuple(tst))
print()

print('Кортеж из одного элемента в Python')
tst = ('1') #строка

tst = (1,) #кортеж

tst = (True) #булевая
print()

print('Альтернативный синтаксис кортежей в Python')
tst = 1, 2, 3, 4 #кортеж

tst = ['12', '34', '56', '78'] #список

tst = '1,2,3,4' #строка
print()

print('Отдельный элемент кортежа в Python')
tpl = (1, 2, 3, 4)
print(tpl[0])

tpl = ('a', 'b', 3, 4, 'c')
print(tpl[2])

tpl = (10, 9, 8, 7, 6)
print(tpl[-1])

print(tpl[-2])

tpl = (1, 2, 3)
SummaIzTupla = tpl[0] + tpl[1] + tpl[2]
print(SummaIzTupla)
print()

print('Изменение элементов в Python')
tpl = ('ab', 'cd', 'ef')
print(tpl[1]) #'cd'
'''
tpl = (4, 6, 8, 10)
res = tpl[-1] + tpl[0]
tpl[1] = res #ошибка
print(res) 
'''
print()

print('Длина кортежа в Python')
tpl = ('1', 'b', '3', 'd', '5')
print(len(tpl))

tpl = (1, 2, 3)
print(len(tpl))
print()

print('Объединение кортежей в Python')
tpl1 = ('1', '2', '3')
tpl2 = ('4', '5', '6')
tpl3 = ('7', '8', '9')
tpl1 += tpl2
tpl1 += tpl3
print(tpl1)

tpl1 = (3, 4)
tpl2 = (1, 2)
tpl2 += tpl1
print(tpl2)
print()

print('Умножение кортежей в Python')
tpl1 = ('1', '2', '3')
print(tpl1 * 3)

tpl1 = ('a', 'b')
tpl2 = (1, 2)
print(tpl1 * 2 + tpl2)
print()

print('Наличие элемента в кортеже в Python')
tpl = (2, 4, 6, 10)
print(8 in tpl) #False

tpl = ('abc', 'def')
print('d' in tpl) #False

tpl = ('1', '2', '3')
res = 1 not in tpl
print(res) #True

tpl1 = ('ac', '3', 4, 'bd', 5)
tpl2 = (1, 2, 3)
res1 = 4 in tpl1
res2 = 2 not in tpl2
print(res1) #True
print(res2) #False
print()

print('Распаковка кортежей в Python')
tpl = ('john', 'smit')
Name, Secondname = tpl
print(Name + ' ' + Secondname)

tpl = (2, 6, 14)
a, b, c = tpl
print(a + b + c)
print()

print('Преобразование в кортеж в Python')
tst = ['a', 'b', 'c', 'd']
print(tuple(tst))

tst = 'abcde'
print(tuple(tst))

tst = 12345
tst = str(tst)
print(tuple(tst))
print()

print('Преобразование кортежа в список в Python')
tpl = ('2', '6', '12')
print(list(tpl))

tpl1 = ('1', '2', '3')
tpl2 = ('4', '5')
tpl1 += tpl2
print(list(tpl1))

tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
lst = sorted(lst, reverse=True)
tpl = tuple(lst)
print(tpl)
print()

print('Слияние кортежа в строку в Python')
tpl = ('1', '2', '3', '4', '5')
print('-'.join(tpl))

tpl = ('1', '2', '3', '4', '5')
print(''.join(tpl))