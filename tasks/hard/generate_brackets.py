"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
generate_brackets(3)
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def _generate_brackets(n, Open, close, s, ans):
    if (Open == n and close == n):
        ans.append(s)
        return
    if (Open < n):
        _generate_brackets(n, Open + 1, close, s + "(", ans)
    if (close < Open):
        _generate_brackets(n, Open, close + 1, s + ")", ans)


def generate_brackets(n):
    ans = []
    _generate_brackets(n, 0, 0, "", ans)
    for s in ans:
        print(s)
