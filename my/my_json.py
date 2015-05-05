#!/usr/bin/env python

import json

print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)

json_str = json.JSONEncoder().encode({"foo": ["bar", "baz"]})
obj = json.JSONDecoder().decode(json_str)
str = json.JSONEncoder().encode(obj)
print str

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

s = "Hello, please split me"
print s.split()
print s.split(",")
