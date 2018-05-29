import paramiko
import time
import csv


def FortiWeb_serverPool(ip, user, passwd, fileDataCSV):
    try:
        session = paramiko.SSHClient()  # Open the session
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, username=user, password=passwd)
        connection = session.invoke_shell()
        connection.send("config server-policy server-pool\n\n\n")
        time.sleep(1)
        with open(fileDataCSV, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                connection.send("edit svp_%s\n\n\n" % row[0])
                connection.send("config  pserver-list\n\n\n")
                connection.send("edit 1\n\n\n")
                connection.send("set ip %s\n\n\n" % row[1])
                connection.send("end\n\n\n")
                connection.send("next\n\n\n")
        connection.send("end\n\n\n")

    except paramiko.AuthenticationException:
        print("wrong credentials")


def Fortiweb_vserver(ip, user, passwd, fileDataCSV):
    try:
        session = paramiko.SSHClient()  # Open the session
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, username=user, password=passwd)
        connection = session.invoke_shell()
        connection.send("config server-policy vserver\n\n\n")
        time.sleep(1)
        with open(fileDataCSV, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                connection.send("edit vs_%s\n\n\n" % row[0])
                # time.sleep(1)
                connection.send("set vip %s\n\n\n" % row[3])
                # time.sleep(1)
                connection.send("set interface port1\n\n\n")
                # time.sleep(1)
                connection.send("next\n\n\n")
                # time.sleep(1)
        connection.send("end\n\n\n")

    except paramiko.AuthenticationException:
        print("wrong credentials")


def Fortiweb_Webpolicy(ip, user, passwd, fileDataCSV):
    try:
        session = paramiko.SSHClient()  # Open the session
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, username=user, password=passwd)
        connection = session.invoke_shell()
        connection.send("config server-policy policy\n\n\n")
        time.sleep(1)
        with open(fileDataCSV, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                connection.send("edit wp_%s\n\n\n" % row[0])
                connection.send("set vserver vs_%s\n\n\n" % row[0])
                connection.send("set server-pool svp_%s\n\n\n" % row[0])
                connection.send("set allow-hosts ALL\n\n\n")
                connection.send("set protocol HTTP\n\n\n")
                connection.send("set service HTTP\n\n\n")
                connection.send(
                    """set web-protection-profile "Inline Medium Level Security"\n\n\n""")
                connection.send(
                    """set waf-autolearning-profile "Default Auto Learn Profile"\n\n\n""")
                connection.send("next\n\n\n")
        connection.send("end\n\n\n")

    except paramiko.AuthenticationException:
        print("wrong credentials")


def FortiGate_VIP(ip, user, passwd, fileDataCSV):
    try:
        session = paramiko.SSHClient()  # Open the session
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, username=user, password=passwd)
        connection = session.invoke_shell()
        connection.send("config firewall vip\n\n\n")
        time.sleep(1)
        with open(fileDataCSV, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] != "":
                    connection.send("""edit "fw_%s"\n\n\n""" % row[0])
                    connection.send("set extip %s\n\n\n" % row[2])
                    connection.send("set mappedip %s\n\n\n" % row[3])
                    connection.send("""set extintf "port9"\n\n\n""")
                    connection.send("set color 26\n\n\n")
                    connection.send("next\n\n\n")
                    time.sleep(1)
        connection.send("end\n\n\n")

    except paramiko.AuthenticationException:
        print("wrong credentials")


def FortiWeb_Delete(ip, user, passwd):
    try:
        session = paramiko.SSHClient()  # Open the session
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, username=user, password=passwd)
        connection = session.invoke_shell()
        connection.send("config server-policy policy\n\n\n")
        time.sleep(1)
        with open('nrru.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                connection.send("delete %s\n\n\n" % row[0])
        connection.send("end\n\n\n")

    except paramiko.AuthenticationException:
        print("wrong credentials")


def Fortiweb_Webpolicy_SSL(ip, user, passwd, fileDataCSV):
    try:
        session = paramiko.SSHClient()  # Open the session
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, username=user, password=passwd)
        connection = session.invoke_shell()
        connection.send("config server-policy policy\n\n\n")
        time.sleep(1)
        with open(fileDataCSV, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                connection.send("edit wp_%s\n\n\n" % row[0])
                connection.send(
                    """set web-protection-profile "Med2"\n\n\n""")
                #connection.send("set https-service HTTPS\n\n\n")
                connection.send("next\n\n\n")
        connection.send("end\n\n\n")

    except paramiko.AuthenticationException:
        print("wrong credentials")


#Fortiweb_vserver("192.168.16.253", "xpop", "Colona@01", "nrru2.csv")
#FortiWeb_serverPool("192.168.16.253", "xpop", "Colona@01", "nrru2.csv")
Fortiweb_Webpolicy_SSL("192.168.16.253", "xpop", "", "nrru2.csv")
