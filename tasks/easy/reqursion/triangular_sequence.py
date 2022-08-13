"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n):
    if n == 1:
        return "1\n"
    else:
        return triangular_sequence(n - 1) + str(n) * n + "\n"


print(triangular_sequence(3))
