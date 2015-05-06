#!/usr/bin/env python


a = 3
b = 5
print a > b
print a < b
print a <= b
print a == b
print a is b
print a is not b
print a in [1, 2, 3, 4, 5]
print a not in [1, 2, 3, 4, 5]
print a > 0 and b > 3
print a < 0 or b < 9

import my_function

my_function.fib(10000)
print dir(my_function)

import future_builtins

print dir(future_builtins)
