"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на 4 пробела

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


Some_list=[1, 2, [1, 2, [5, 7], 3], 8]
def line_print(some_list, n=0):
    for i in range(len(some_list)):
        if isinstance(some_list[i], list):
            line_print(some_list[i], n+1)
        else:
            print(("    ")*n+str(some_list[i]))

line_print(Some_list)
print(range(len(Some_list)))
print(Some_list[2])
print(len([1, 2, [1, 2, [5, 7], 3], 8]))
print(("\t")*3+str(2))