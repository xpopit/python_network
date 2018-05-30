#!/usr/local/bin/python3.6
import paramiko
import time
import re

ip = '223.27.243.98'
user = 'itgreen'
passwd = 'ITG@1234'

client = paramiko.SSHClient()  # Open the session
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, username=user, password=passwd)
stdin, stdout, stderr = client.exec_command('show full-configuration\n')
with open('backup.tmp', 'w') as backup_tmp:
    for line in stdout:
        backup_tmp.write(line)
with open('backup.tmp', 'r') as f:
    content = f.read()
content_new = re.sub('^.*--More--\s+\n',
                     r'', content, flags=re.M)

with open('backup.conf', 'w') as backup:
    backup.write(content_new)

print(content_new)
client.close()
