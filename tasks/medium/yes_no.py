"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


INT_VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 123, 1244, 4, 5, 6, 7, 8, 9, 10]


def yes_or_no(int_value):
    all_freq = {}
    for i in int_value:
        if i in all_freq:
            print("Yes")
        else:
            all_freq[i] = 1
            print("No")
    pass


print(yes_or_no(INT_VALUE))
