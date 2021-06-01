#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
       print("Неверный размер списка", file=sys.stderr)
       exit(1)
    s = 0
    for item in A:
       if not ((item % 2) == 0):
          s += item
    x0 = 0  # Позиция первого отрицательного элемента
    x1 = 0  # Позиция последнего отрицательного элемента
    for i, a in enumerate(A):
        if a < 0:
            x0 = i
            break
    for i, a in enumerate(A[::-1]):
        if a < 0:
            x1 = len(A) - 1 - i
            break
    print(s)
    print(sum(A[x0 + 1:x1]))

snew=list(filter(lambda x: abs(x)>1, A))
for _ in range(len(A)-len(snew)): snew.append(0)
print(snew)