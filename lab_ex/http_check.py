import paramiko
import csv
import re
import subprocess as sp
import requests


def HttpPing(Host):
    try:
        r = requests.get('http://%s' % Host, timeout=0.5)
        if r.status_code == 200:
            return ("%s -> !UP" % Host)
        else:
            return ("%s -> !Down" % Host)
    except:
        return ("%s -> !Down" % Host)


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def ipcheck(pop):
    status, result = sp.getstatusoutput("ping -c1 " + pop)
    if status == 0:
        return(pop + " is UP !")
    else:
        return(pop + " is DOWN !")


with open('nrru.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2]:
            with open('onfortigate.csv', newline='') as f2:
                reader2 = csv.reader(f2)
                for row2 in reader2:
                    if findWholeWord(row[2])(row2[1]):
                        print(row, row2, "," +
                              HttpPing(row[1]), "," + HttpPing(row[2]))
        else:
            print(row)
