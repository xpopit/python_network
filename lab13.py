import csv
conf = '''edit "{name}"
    set vdom "root"
    set ip {ip}
    set allowaccess ping https ssh http fgfm
    set type physical
    set role lan
next'''

with open('fgt_int.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(conf.format(name=('%s' % row[0]), ip=(
            '%s' % row[1])))
