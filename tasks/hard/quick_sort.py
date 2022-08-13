"""
БЫСТРАЯ СОРТИРОВКА
Этот алгоритм также относится к алгоритмам «разделяй и властвуй».
Его используют чаще других алгоритмов, описанных в этой статье.
При правильной конфигурации он чрезвычайно эффективен и не требует
дополнительной памяти, в отличие от сортировки слиянием.
Массив разделяется на две части по разные стороны от опорного элемента.
В процессе сортировки элементы меньше опорного помещаются
перед ним, а равные или большие — позади.

Быстрая сортировка начинается с разбиения списка и выбора одного из элементов в
качестве опорного. А всё остальное передвигаем так, чтобы этот элемент встал
на своё место. Все элементы меньше него перемещаются влево,
а равные и большие элементы перемещаются вправо.

Существует много вариаций данного метода. Способ разбиения массива,
рассмотренный здесь, соответствует схеме Хоара (создателя данного алгоритма).

Обратите внимание, что алгоритм быстрой сортировки будет работать медленно,
если опорный элемент равен наименьшему или наибольшему элементам списка.
При таких условиях, в отличие от сортировок кучей и слиянием, обе из которых имеют в
худшем случае время сортировки O(n log n), быстрая сортировка в
худшем случае будет выполняться O(n²).

ВРЕМЯ СОРТИРОВКИ: в среднем O(n log n)
"""

import random


def quicksort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
    l_A = [n for n in A if n < q]

    e_A = [q] * A.count(q)
    b_A = [n for n in A if n > q]
    return quicksort(l_A) + e_A + quicksort(b_A)
