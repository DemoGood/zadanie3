#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Введите значение x: "))
    '''
    В нашем примере x находится в числители,
    значит, может принимать любое значение
    '''
    a = (x ** 2) / 4
    S, n = a, 1

    while math.fabs(a) > EPS:
        a *= (x ** 2) / ((4 * n + 4) * (2 * n + 1))
        S += a
        n += 1

    print(f"{S}")
