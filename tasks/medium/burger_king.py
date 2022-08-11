"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""


def bread(func):
    def wrapper(*args, **kwargs):
        print("</------------\\>")
        result = func(*args, **kwargs)
        print("<\\____________/>")
        return result
    return wrapper

def tomato(func):
    def wrapper(*args, **kwargs):
        print("*** помидоры ****")
        result = func(*args, **kwargs)
        return result
    return wrapper

def salad(func):
    def wrapper(*args, **kwargs):
        print("~~~~ салат ~~~~~")
        result = func(*args, **kwargs)
        return result
    return wrapper

def cheese(func):
    def wrapper(*args, **kwargs):
        print("^^^^^ сыр ^^^^^^")
        result = func(*args, **kwargs)
        return result
    return wrapper

def onion(func):
    def wrapper(*args, **kwargs):
        print("----- лук ------")
        result = func(*args, **kwargs)
        return result
    return wrapper
@bread
@onion
@tomato
def beef():
    print("### говядина ###")
@bread
@cheese
@salad
def chicken():
    print("|||| курица ||||")



print(beef())
print(chicken())