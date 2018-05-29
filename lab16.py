#!/usr/local/bin/python3.6

import subprocess
ipaddr = "8.8.8.8"
#result = subprocess.call("ping -c 3 www.google.com", shell=True)
result = subprocess.check_output(
    "ping -c 3 %s" % ipaddr, shell=True)
# print(type(result))
print(result.decode("utf-8"))
