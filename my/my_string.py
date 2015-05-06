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