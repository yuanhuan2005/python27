#!/usr/bin/env python

import sys

print sys.argv[0]


the_world_is_flat = 0
if the_world_is_flat:
    print "Be careful not to fall off!"
else:
    print "that's ok"


import os
print os.environ.data
print os.environ.get('PUBLIC')
filename = "E:\\BaiduYunDownload\\rarreg.key"
print filename
if filename and os.path.isfile(filename):
    print "ok"
    open(filename, 'r').read()
else:
    print "fail"

import math
print math.log10(2)
print math.sin(10)

import json
print json.__version__
print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)

json_str = json.JSONEncoder().encode({"foo": ["bar", "baz"]})
obj = json.JSONDecoder().decode(json_str)
str = json.JSONEncoder().encode(obj)
print str

import site

print site.getusersitepackages()

print round(3 / 7.0, 4)
print "doesn\'t"
hello = "This is a test file\n" \
        "and that is ok\n" \
        "end"
print hello
hello = "This is a test file\n\
    and that is ok\n\
    end"
print hello

import this

print this

from time import sleep

sleep(0.3)
print "sleep done"

import platform

print platform.platform()

import os.path

print os.path
print os.path.abspath(".")

import subprocess

print "\n"
subprocess.call("ls -l")
subprocess.call("uname -a")
subprocess.call("netstat -an")

