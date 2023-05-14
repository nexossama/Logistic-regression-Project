def ConvertSchool(l):
    if l[0]=="GP":
        return 0
    if l[0]=="MS":
        return 1

def ConvertSex(l):
    if l[1]=="M":
        return 1
    if l[1]=="F":
        return 0

def ConvertAddress(l):
    if l[3]=="U":
        return 1
    if l[3]=="R":
        return 0

def ConvertFamsize(l):
    if l[4]=="LE3":
        return 1
    if l[4]=="GT3":
        return 0

def ConvertPstatus(l):
    if l[5]=="T":
        return 0
    if l[5]=="A":
        return 1

def ConvertMedu(l):
    if l[6]==0:
        return 0
    if l[6]==1:
        return 1
    if l[6]==2:
        return 2
    if l[6]==3:
        return 3
    if l[6]==4:
        return 4

def ConvertFedu(l):
    if l[7]==0:
        return 0
    if l[7]==1:
        return 1
    if l[7]==2:
        return 2
    if l[7]==3:
        return 3
    if l[7]==4:
        return 4


def ConvertMjob(l):
    if l[8]=="teacher":
        return 1
    if l[8]=="health":
        return 3
    if l[8]=="services":
        return 2
    if l[8]=="at_home":
        return 0
    if l[8]=="other":
        return 4

def ConvertFjob(l):
    if l[8] == "teacher":
        return 1
    if l[8] == "health":
        return 3
    if l[8] == "services (e.g. administrative or police)":
        return 2
    if l[8] == "at_home":
        return 0
    if l[8] == "other":
        return 4


def ConvertData(l):
    data = [ConvertSchool(l),ConvertSex(l),l[2],ConvertAddress(l),ConvertFamsize(l),ConvertPstatus(l),ConvertMedu(l),ConvertFedu(l),ConvertMjob(l),ConvertFjob(l)]
    return data

def ConvertClass(x):
    if x==0 :
        return "Failing"
    if x==1:
        return "Successful"



