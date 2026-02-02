print('Создание списков с помощью квадратных скобок в Python')
spisok = ['ab', 'cd', 'ef']
print(spisok)

DniNedeli = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(DniNedeli)

DniNedeli = ['Monday', 2, 'Tuesday', 3, 'Wednesday', 4, 'Thursday', 5, 'Friday', 6, 'Saturday', 7, 'Sunday', 8]
print(DniNedeli)
print()

print('Создание списков с помощью функции list в Python')
tst = list('abcde')
print(tst) #['a', 'b', 'c', 'd', 'e']

tst = list('a12b')
print(tst) #['a', '1', '2', 'b']
'''
tst = list(5678)
print(tst) #ошибка
'''
tst = list('4321')
print(tst) #['4', '3', '2', '1']
print()

print('Разбиение строки в список в Python')
txt = 'a,b,c,d,e'
print(txt.split(',')) #['a', 'b', 'c', 'd', 'e']

txt = 'a_bc_de'
print(txt.split('_')) #['a', 'bc', 'de']

txt = '1 23 45'
print(txt.split(' ')) #['1', '23', '45']

txt = '123_45'
print(txt.split()) #['123_45']
print()

print('Получение отдельного элемента списка в Python')
lst = [1, 2, 3, 4, 5]
print(lst[0])

lst = [1, 2, 3, 4, 5]
print(lst[1])

lst = [1, 2, 3, 4, 5]
print(lst[-1]) #5

lst = [2, 4, 6, 8]
res = lst[3] - lst[0]
print(res) #6
print()

print('Длина списка в Python')
lst = ['a', 'b', 'c', 'd']
print(len(lst))

tst = '12abc45'
tst = list(tst)
print(len(tst))
print()

print('Последний элемент списка в Python')
lst = ['a', 'b', 'c', 'd']
print(lst[-1])
print(lst[-2])
print()

print('Изменение элементов списка в Python')
lst = [1, 2, 3, 4, 5]
lst[1] = 10
print(lst)

lst = ['a', 'b', 'c', 'd']
lst[-1] = True
print(lst)

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
lst1[-1] = lst2[-1]
print(lst1)
print()

print('Добавление элементов в конец списка в Python')
lst = [1, 2, 3, 4, 5]
lst.append(13)
print(lst)

lst = []
lst.append(1)
print(lst)

lst = []
lst.append('a')
lst.append('b')
lst.append('c')
print(lst)
print()

print('Добавление элементов по позиции в список в Python')
lst = [1, 2, 3, 4, 5]
lst.insert(2, 'a')
print(lst)

lst = [1, 2, 3, 4, 5]
lst.insert(0, 'a')
print(lst)

lst = [3, 6, 12]
lst.insert(2, 9)
print(lst)
print()

print('Объединение списков методом extend в Python')
lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst1.extend(lst2)
print(lst1)

lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst3 = [1, 2, 3]
lst1.extend(lst3)
lst1.extend(lst2)
print(lst1)
print()

print('Объединение списков в Python')
lst1 = [4, 5, 6]
lst2 = [1, 2, 3]
lst3 = lst2 + lst1
print(lst3)

lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst3 = [1, 2, 3]
spisok = lst1 + lst2 + lst3
print(spisok)
print()

print('Добавление в список в Python')
lst1 = ['12', '34', '56']
lst2 = ['ab', 'cd', 'ef']
lst1 += lst2
print(lst1)

lst1 = ['a', 'b', 'c']
lst2 = [4, 5, 6]
lst2 += lst1
print(lst2)
print()

print('Удаление элементов из списка оператором del в Python')
lst = ['a', 'b', 'c', 'd', 'e']
del lst[0]
print(lst)

lst = ['a', 1, 'b', 2, 'c', 3]
del lst[1]
del lst[2]
del lst[3]
print(lst)
print()

print('Удаление элементов из списка по их значению в Python')
lst = ['a', 'b', 'c', 'd', 'e']
lst.remove('c')
print(lst)

lst = ['a', 'b', 'c', 'd', 'e']
lst.remove('b')
print(lst)

lst = ['b', 1, 2, 'b', 'c', 2]
lst.remove('b')
lst.remove(2)
print(lst)
print()

print('Получение и удаление элемента из списка в Python')
lst = ['a', 'b', 'c', 'd', 'e']
print(lst.pop(-1))

lst = ['a', 'b', 'c', 'd', 'e']
print(lst.pop(0))

lst = ['a', 'b', 'c', 'd', 'e']
print(lst.pop(1))
print()

print('Удаление всех элементов из списка в Python')
lst = ['a', 'b', 'c', 'd', 'e']
lst.clear()
print(lst)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1 += lst2
lst2.clear()
print(lst1)
print(lst2)
print()

print('Поиск индекса элемента по его значению в Python')
lst = ['a', 'b', 'c', 'd', 'e']
print(lst.index('c'))

lst = ['a', 'b', 'c', 'b', 'd']
print(lst.index('b', 2)) #забавно, что значание с индексом -1 не обозначается, как _stop

lst = ['ab', 12, 'cd', 34]
tst = 'cd'
print(lst.index(tst)) #2
'''
lst = [1, 3, 'a', 'b', 3, 6]
tst = 2
print(lst.index(tst)) #ошибка
'''
print()

print('Проверка наличия элемента в списке в Python')
lst = ['a', 'b', 'c', 'd', 'e']
print('c' in lst) #решил не задавать лишнюю переменную

lst = ['a', 'b', 'c', 'd']
res = 'e' in lst
print(res) #False

lst = ['a', 1, 'b', 3, 'c']
res = 3 in lst
print(res) #True
print()

print('Подсчет элементов в списке в Python')
lst = ['a', 'b', 'c', 'd']
print(lst.count('c')) #1

lst = ['1', 'b', '2', 'd']
print(lst.count(1)) #0

lst = ['ab', '12', 2, 'cd', 1, 2]
print(lst.count(2)) #2
print()

print('Обратный порядок элементов в списке в Python')
lst = ['a', 'b', 'c', 'd']
lst.reverse()
print(lst) #['d', 'c', 'b', 'a']

lst = [10, 4, 8, 2]
lst.reverse()
print(lst) #[2, 8, 4, 10]
print()

print('Сортировка элементов в исходном списке в Python')
lst = [4, 2, 5, 1, 3]
lst.sort()
print(lst)

lst = [4, 2, 5, 1, 3]
lst.sort(reverse = True)
print(lst)

lst = [1, 2, 3, 4, 5]
lst.sort(reverse = True)
print(lst)

lst1 = ['a', 'b', 'c']
lst2 = [3, 2, 1]
lst1.sort(reverse = True)
lst2.sort()
print(lst2 + lst1)
print()

print('Сортировка элементов в копии списка в Python')
lst = ['d', 'c', 'b', 'a']
print(sorted(lst))

lst = [4, 12, 24]
print(sorted(lst, reverse=True))

lst = [10, 8, 6, 4]
print(sorted(lst))
print()

print('Слияние списка в строку в Python')
lst = ['a', 'b', 'c', 'd', 'e']
print('-'.join(lst))

lst = ['a', '1', 'b', '2']
res = ''.join(lst)
print(res) #просто строка, т.к. нет значения разделителя

'''ошибка
lst = ['1', '2', 3, '4']
res = '/'.join(lst)
print(res)
'''

lst = ['4', '3', '2', '1']
sortirovan = sorted(lst)
print(''.join(sortirovan))