#!/usr/bin/env python

filename = "E:\\test.txt"
f = open(filename, "r")

# for, most simple way
for line in f:
    print line

# while, same efficiency as last for
line = f.readline()
while line:
    print line
    line = f.readline()

# more efficiency
while True:
    lines = f.readlines(100000)
    if not lines:
        break
    for line in lines:
        print line

f.close()