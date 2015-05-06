#!/usr/bin/env python

t = 12345, 54321, 'hello!'
print t.count(12341)
print len(t)

t = (1, 2)
l = [1, 2]
s = {1, 2}
r = 1, 2
d = {"age": 2}
print d.keys()
print type(t)
print type(l)
print type(s)
print type(r)
print type(d)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

for i in reversed(range(0, 10, 4)):
    print i

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f



