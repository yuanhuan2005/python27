import os

os.system("ls")

import subprocess

subprocess.call("ls")

import sys

print sys.argv
print sys.argv[0]

sys.stderr.write('Warning, log file not found starting a new one\n')

sys.stdout.write("INFO | going to down")
sys.exit(0)