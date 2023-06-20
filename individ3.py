#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    i = 1
    n = int(input("Введите n: "))
    # Делители числа меньше или равны половине самого числа
    while i <= (n + 1) / 2:
        if n / i == n // i:
            print(i, end=' ')  # end= акой символ или строка выводить после вывода (всех) значений
        i += 1

    if n != 1:
        print(n)
