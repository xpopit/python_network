#!/usr/local/bin/python3.6

import textfsm
import sys
conf = '''edit "{name}"
    set vdom "root"
    set ip {ip}
    set allowaccess ping https ssh http fgfm
    set type physical
    set role lan
next'''

# Open the template file, and initialise a new TextFSM object with it.
template_file = sys.argv[1]
fsm = textfsm.TextFSM(open(template_file))

# Read stdin until EOF, then pass this to the FSM for parsing.
input_data = sys.stdin.read()
fsm_results = fsm.ParseText(input_data)

for row in fsm_results:
    if row[0] == "mgmt":
        row[0] = "Lan"
    # elif row[0] == "default":
    #    break
    # print(row)
    print(conf.format(name=('%s' % row[0]), ip=(
        '%s' % row[2])))
