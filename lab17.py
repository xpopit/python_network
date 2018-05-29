#!/usr/local/bin/python3.6

import subprocess
# result = subprocess.call(['df', '-h'])
p = subprocess.Popen(["traceroute", "8.8.8.8"], stdout=subprocess.PIPE)

print(p.communicate())
