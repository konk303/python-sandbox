#!/usr/bin/env python3

from functools import reduce

print(reduce((lambda results, i: results if i < 2 else results + [results[i -2] + results[i - 1]]), range(100), [1, 1]))

def fib(nth):
    if nth < 2:
        return 1
    return fib(nth -2) + fib(nth - 1)

for i in range(10): print('fib %s: %s' % (i, fib(i)))
