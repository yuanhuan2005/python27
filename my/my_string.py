#!/usr/bin/env python

print "doesn\'t"
print r"doesn\'t"
print "This is a test file\n" \
      "and that is ok\n" \
      "end"
print "This is a test file\n\
    and that is ok\n\
    end"
print """
Usage: setuid -u UID
     -h         Display this usage message
     -u         UID of you
"""

print "abc".startswith("a")

print "jason" " " "fei"
print "Jason".strip()

word = "helloworld"
print word[0:5] + " python"
print word[-10]

s = 'Hello, world.'
print str(s)
print repr(s)
print str(1 / 9.0)
print repr(1 / 9.0)

hello = 'hello, world\n'
print repr(hello)
print str(hello)

for x in range(1, 11):
    print str(x).rjust(2), str(x * x).rjust(3), str(x * x * x).rjust(4)

print '12'.zfill(5)

print 'We are the {} who say "{}!"'.format('knights', 'Ni')
print '{0} and {1}'.format('spam', 'eggs')
print '{1} and {0}'.format('spam', 'eggs')

import math

print 'The value of PI is approximately {}.'.format(math.pi)
print 'The value of PI is approximately {!r}.'.format(math.pi)
print('The value of PI is approximately {0:.4f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone)

print 'The value of PI is approximately %5.3f.' % math.pi
