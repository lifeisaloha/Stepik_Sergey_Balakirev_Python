"""
7.5 Функции с произвольным числом параметров (задача 1)

Подвиг 3. Объявите функцию с именем get_even, которая принимает произвольное количество чисел в качестве аргументов и возвращает список, составленный только из четных переданных значений.

Функцию выполнять не нужно, только определить.

Sample Input:

45 4 8 11 12 0
Sample Output:

4 8 12 0
"""


def get_even(*number):
    lst = []
    for i in number:
        if i % 2 == 0:
            lst.append(i)
    return lst


s = input().strip()
res = get_even(*map(int, s.split()))
print(*res)
