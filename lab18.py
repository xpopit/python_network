#!/usr/local/bin/python3.6

import subprocess
import textfsm
ipaddr = "8.8.8.8"
# result = subprocess.call("ping -c 3 www.google.com", shell=True)
result = subprocess.check_output(
    "ping -c 10 %s" % ipaddr, shell=True)
# print(type(result))
# print(result.decode("utf-8"))
# print(type(result.decode()))
fsm = textfsm.TextFSM(open("averageOfping.tmpl"))
# fsm_results = fsm.ParseText(result)
fsm_results = fsm.ParseText(result.decode())

average = 0
# print(fsm_results)
# print(type(fsm_results))
for row in fsm_results:
    # print(row)
    average += float(row[0])

print("ค่าเฉลี่ย: %s ms" % str(round((average % len(fsm_results)), 3)))
