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


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refused user')
        print complaint


# ask_ok("Do you really want to quit? [yes/no]")

