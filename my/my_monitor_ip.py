from platform import system

curr_os = system()

cmd = ""
ip_address = "220.181.30.53"
ping_count = 2
if curr_os == "Linux":
    cmd = "ping -c " + str(ping_count) + " " + ip_address
elif curr_os == "Windows":
    cmd = "ping -n " + str(ping_count) + " " + ip_address
else:
    from sys import exit

    exit(1)

print cmd

import os
import re

r = os.popen(cmd)
text = r.read()
r.close()

dbl = int(re.findall(r"\d*%", text).pop(0).replace("%", ""))
print int(dbl)

avg = 0
if curr_os == "Windows":
    avg = int(re.findall(r"\d*ms$", text).pop(0).replace("ms", ""))
else:
    cmd += " | grep 'rtt min/avg/max/mdev' | awk '{print $4}' | awk -F/ '{print $2}'"
    r = os.popen(cmd)
    avg = r.read()
    r.close()

print int(avg)
