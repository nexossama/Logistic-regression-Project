def ConvertSchool(l):
    if l[0]=="Gabriel Pereira":
        return 0
    if l[0]=="Mousinho da Silveira":
        return 1

def ConvertSex(l):
    if l[1]=="Male":
        return 1
    if l[1]=="Female":
        return 0

def ConvertAddress(l):
    if l[3]=="urban":
        return 1
    if l[3]=="rural":
        return 0

def ConvertFamsize(l):
    if l[4]<=3:
        return 1
    if l[4]>3:
        return 0

def ConvertPstatus(l):
    if l[5]=="living together":
        return 0
    if l[5]=="apart":
        return 1

def ConvertMedu(l):
    if l[6]=="none":
        return 0
    if l[6]=="primary education (4th grade)":
        return 1
    if l[6]=="5th to 9th grade":
        return 2
    if l[6]=="secondary education":
        return 3
    if l[6]=="higher education":
        return 4

def ConvertFedu(l):
    if l[7]=="none":
        return 0
    if l[7]=="primary education (4th grade)":
        return 1
    if l[7]=="5th to 9th grade":
        return 2
    if l[7]=="secondary education":
        return 3
    if l[7]=="higher education":
        return 4


def ConvertMjob(l):
    if l[8]=="teacher":
        return 1
    if l[8]=="health : care related":
        return 3
    if l[8]=="services (e.g. administrative or police)":
        return 2
    if l[8]=="at_home":
        return 0
    if l[8]=="other":
        return 4

def ConvertFjob(l):
    if l[8] == "teacher":
        return 1
    if l[8] == "health : care related":
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



