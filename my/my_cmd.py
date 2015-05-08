import os

cmd = "ls"
os.system(cmd)

import subprocess

subprocess.call(cmd)

import os

r = os.popen(cmd)
text = r.read()
r.close()
print text

import sys

print sys.argv
print sys.argv[0]

sys.stderr.write('Warning, log file not found starting a new one\n')
sys.stdout.write("INFO | going to down")
sys.exit(0)
