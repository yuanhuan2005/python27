#!/usr/bin/env python


import math

print math.log10(2)
print math.sin(10)

print round(3 / 7.0, 4)

print math.pi

print "sum: " + repr(sum(i * i for i in range(19)))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print "sum: " + repr(sum(x * y for x, y in zip(xvec, yvec)))

filename = "E:\\test.txt"
page = open(filename, "r")
unique_words = set(word for line in page for word in line.split())
page.close()
print unique_words