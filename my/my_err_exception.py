#!/usr/bin/env python


filename = "E:\\test.txt"
not_found_file = "not_found.txt"

# no exception occurs
try:
    f = open(filename)
except IOError as e:
    print "IO error({0}): {1}".format(e.errno, e.strerror)
else:
    print "file opened."
    f.close()
finally:
    print "file safely closed."

# exception occurs
print ""
try:
    f = open(not_found_file)
except IOError as e:
    print "IO error({0}): {1}".format(e.errno, e.strerror)
else:
    print "file opened."
    f.close()
finally:
    print "file safely closed."

# throw a exception
print ""
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)
    print inst.args
    print inst
    x, y = inst.args
    print 'x =', x
    print 'y =', y


# catch exception throwing by function
print ""


def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as detail:
    print 'Handling run-time error:', detail

# throw a exception
# raise NameError('Hi There')

class MyError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return repr(self.error_message)


try:
    raise MyError("not good")
except MyError as e:
    print 'My exception occurred, message:', e.error_message

