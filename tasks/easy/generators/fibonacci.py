"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci(fib_1=0, fib_2=1):
    while True:
        yield max(fib_1,fib_2)
        if fib_1>fib_2:
            fib_2 += fib_1
        else:
            fib_1 += fib_2