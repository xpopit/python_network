import subprocess as sp


def ipcheck(pop):
    status, result = sp.getstatusoutput("ping -c1 " + pop)
    if status == 0:
        print("System " + pop + " is UP !")
    else:
        print("System " + pop + " is DOWN !")


ipcheck("1.1.4.1")
