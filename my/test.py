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
