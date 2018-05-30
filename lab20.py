#!/usr/local/bin/python3.6
import paramiko
import time
import csv

ip = '223.27.243.98'
user = 'itgreen'
passwd = 'ITG@1234'

session = paramiko.SSHClient()  # Open the session
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(ip, username=user, password=passwd)
connection = session.invoke_shell()
connection.send("config firewall address\n\n\n")
time.sleep(1)
with open("addr.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        connection.send("edit ts_%s\n\n\n" % row[0])
        connection.send("set subnet %s\n\n\n" % row[1])
        connection.send("next\n\n\n")
connection.send("end\n\n\n")
