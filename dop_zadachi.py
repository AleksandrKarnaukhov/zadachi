m = int(input("количество строк матрицы: "))
n = int(input("количество значений в каждом из столбцов: "))
k = int(input("значение, которым столбцы заполняются: "))

list1 = []
for i in range(m):
    list2 = []
    for j in range(n):
        list2.append(k)
    list1.append(list2)
print(list1)