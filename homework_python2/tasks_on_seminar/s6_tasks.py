#task 39
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива





# task41
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# a = [1, 5, 1, 5, 1]
# # a = [1, 2, 1, 2, 1,5,2,6,3] test

c = []
# for i in range (1,len(a),2):
#     if a[i+1] < a[i] > a[i-1]:
#         counter =+ 1
#         c.append(a[i])
#         print(c)
#
#         # print(len(c))
#     if a[i] < a[i + 1]:
#         print(0)
# print(len(c))
l = int(input('enter length > 3  '))
if l % 2 == 0:
    l = l + 1
a = [input(i ) for i in range(l)]

def v (a,c):
    for i in range(1, len(a), 2):
        if a[i + 1] < a[i] > a[i - 1]:
           c.append(a[i])
    if a[i] < a[i + 1]:
        print(0)
    return len(c)
print(v(a,c))


