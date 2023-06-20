#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x = int(input("Введите x: "))
    y = int(input("Введите y: "))
    # Деление с остатком
    a = x / y
    # Деление без остатка
    b = x // y
    if a != b:
        print("x не делится нацело.")
    else:
        print("x делится нацело.")
