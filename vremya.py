import datetime
import calendar
import time

print('Работа с датами в Python')
#Задача 1, 2, 3, 4
birthdate = datetime.date(2002, 2, 10)
print(birthdate)
print(f'{birthdate.year} {birthdate.day} {birthdate.month}')
print()

print('Вывод текущей даты в Python')
#Задача 1, 2, 3
date1 = datetime.date.today()
print(f'{date1.day} {date1.month} {date1.year}')
print()

print('Получение дня недели в Python')
#Задача 1
date2 = datetime.date(2026, 2, 27)
print(date2.isoweekday())

#Задача 2
if date2.weekday() in range(0, 5):
    print('Рабочий день')
else:
    print('Выходной день')

#Задача 3
date3 = datetime.date(2026, 11, 2)
print(f'{date3.weekday()} {date3.isoweekday()}')
print()

print('Разность двух дат в Python')
#Задача 1
dt1 = '13/10/2018 22:15:45'
dt2 = '15/11/2018 09:47:16'
date1 = datetime.datetime.strptime(dt1, '%d/%m/%Y %H:%M:%S')
date2 = datetime.datetime.strptime(dt2, '%d/%m/%Y %H:%M:%S')
difference = date2 - date1
print(difference)

#Задача 2
dt1 = '01-12-2025 16:07:5'
dt2 = '31:12:2025 10:32:45'
start_dt = datetime.datetime.strptime(dt1, '%d-%m-%Y %H:%M:%S')
end_dt = datetime.datetime.strptime(dt2, '%d:%m:%Y %H:%M:%S')
diff = end_dt - start_dt
print(diff)
print()

print('Определение високосного года в Python')
#Задача 1
year = 2000
print(calendar.isleap(year))

#Задача 2
year = 1910
print(calendar.isleap(year))

#Задача 3
Nowadays = datetime.datetime.now().year
print(calendar.isleap(Nowadays))
print()

print('Вывод времени в Python')
#Задача 1
Nowadays = datetime.datetime.now()
print(f'{Nowadays.hour}:{Nowadays.minute}:{Nowadays.second}')

#Задача 2
print(datetime.datetime.now())
print()

print('Форматирование даты в Python')
#Задача 1
tdy = datetime.datetime.now()
dmy = tdy.strftime('%d.%m.%Y')
print(dmy)

#Задача 2
tdy = datetime.datetime.now()
dmy = tdy.strftime('%H:%M:%S %d.%m.%Y:%w')
print(dmy)
print()

print('Получение времени в формате epoch в Python')
print(time.time())
print()

print('Получение даты из формата epoch в Python')
tdy = time.time()
ttt = time.ctime(tdy)
print(ttt)
print()

print('Преобразование формата epoch в объект struct_time в Python')
#Задача 1
tdy = time.time()
Nowd = time.localtime(tdy)
print(Nowd)
print(Nowd.tm_mday)

#Задача 2
print(Nowd.tm_hour)

#Задача 3
dt = 1602314100.0
Nowadays = time.localtime(dt)
print(Nowadays)
print()

print('Получение объекта struct_time по UTC в Python')
tdy = time.time()
Gmtime_tdy = time.gmtime()
print(Gmtime_tdy)
print()

print('Получение формата epoch из struct_time в Python')
tdy = time.time()
Gmtime_tdy = time.gmtime()
Sec = time.mktime(Gmtime_tdy)
print(Sec)
print()

print('Разность эпох в Python')
#Задача 1
dt = '24/07/2015 16:1'
dt1 = time.strptime(dt, '%d/%m/%Y %H:%M')
dt2 = time.mktime(dt1)
tdy = time.time()
print(tdy - dt2)

#Задача 2
dt1 = '12/02/2023 10:12:54'
dt2 = '31/12/2024 19:38:21'

date1 = time.strptime(dt1, '%d/%m/%Y %H:%M:%S')
date2 = time.strptime(dt2, '%d/%m/%Y %H:%M:%S')


MK_date1 = time.mktime(date1)
MK_date2 = time.mktime(date2)

print(MK_date2 - MK_date1)

#Задача 3
print((MK_date2 - MK_date1)//(3600*24))
print()

print('Задержка выполнения операции в Python')
#Задача 1
time.sleep(2) #15 сек это долго
print('sanya')

#Задача 2
lst = ['a', 'b', 'c', 'd']
for i in lst:
    time.sleep(3)
    print(i, end=' ')




























