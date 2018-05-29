#!/usr/local/bin/python3.6

import textfsm
import sys

# Open the template file, and initialise a new TextFSM object with it.
template_file = sys.argv[1]
fsm = textfsm.TextFSM(open(template_file))

# Read stdin until EOF, then pass this to the FSM for parsing.
input_data = sys.stdin.read()
print(type(input_data))
fsm_results = fsm.ParseText(input_data)

# print('Header:')
print(fsm.header)

for row in fsm_results:
    print(row)
    #print('%s %s' % (row[2], row[3]))
