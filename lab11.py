#!/usr/bin/env python3.6
conf = '''edit "{name}"
    set vdom "root"
    set ip {ip}
    set allowaccess ping https ssh http fgfm
    set type physical
    set role lan
next'''
for x in range(0, 100):
    print(conf.format(name=('port%s' % x), ip=(
        '192.168.%s.254 255.255.255.0' % x)))
