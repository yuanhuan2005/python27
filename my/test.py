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

import site

print site.getusersitepackages()

from time import sleep
sleep(0.3)
print "sleep done"


import os.path

print os.path
print os.path.abspath(".")

import subprocess

print "\n"
subprocess.call("ls -l")
subprocess.call("uname -a")

import array

print array.ArrayType
