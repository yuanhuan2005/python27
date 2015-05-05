#!/usr/bin/env python

x = 0
try:
    x = int(raw_input("Please enter an integer: "))
except:
    print "Error: not a number"

# if/elif/else
print "\nif/elif/else:"
print x
if x < 0:
    print "negative"
elif x > 0:
    print "positive"
else:
    print "zero"

# for
print "\nfor:"
a = ['cat', 'window', 'defenestrate']
for x in a:
    print x

for i in range(0, 10, 3):
    print i

# while
print "\nwhile:"
n, m = 0, 1
while m < 100:
    print m
    n, m = m, n + m



# break/contine
print "\nbreak/contine:"
m = 0
while True:
    print m,
    m += 1
    if m > 100:
        break
    else:
        continue

# pass
i = 0
while i < 100:
    pass
    i += 1

