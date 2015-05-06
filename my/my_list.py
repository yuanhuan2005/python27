#!/usr/bin/env python

# define and init
a = ["a", "b", "c", "d"]
b = ["1", "2", a, "4"]

# length
print "\nlength:"
print len(a)
print len(b)

# range
print "\nrange:"
print a[1:3]
print b[1:3]
print a[1]

# modify item
print "\nmodify item:"
a[1] = a[1] + "_plus"
print a[1]
print a
print b

# remove some
print "\nremove some:"
a[3:4] = []
del a[0]
print a
print b

# insert some
print "\ninsert some:"
a[3:4] = ["999", "888"]
print a
print b

# append some
print "\nappend some:"
a.append("new_append")
print a
print b

from collections import deque

queue = deque(["Eric", "John", "Michael"])
print queue