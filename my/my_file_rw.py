#!/usr/bin/env python

filename = "E:\\test.txt"
f = open(filename, "r")

# for, most simple way
for line in f:
    print line
f.close()

# while, same efficiency as last for
f = open(filename, "r")
line = f.readline()
while line:
    print line
    line = f.readline()
f.close()

# more efficiency
f = open(filename, "r")
while True:
    lines = f.readlines(100000)
    if not lines:
        break
    for line in lines:
        print line
f.close()

import datetime

f = open(filename, "a")
f.write(str(datetime.datetime.now()) + "\n")
f.close()

f = open(filename, "r")
for line in f:
    print line
f.close()
