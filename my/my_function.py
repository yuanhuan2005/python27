#!/usr/bin/env python

def fib(n):
    x, y = 0, 1
    while y < n:
        print y,
        x, y = y, x + y
    print ""

    return y


def fib1(n):
    x, y = 0, 1
    while y < n:
        x, y = y, x + y
        print x,
    print ""

    return y


fib(10000)
fib1(10000)