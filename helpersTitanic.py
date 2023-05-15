def ConvertAge(l):
    if l[1]<=10:
        return 0
    if l[1]>10 and l[1]<=20:
        return 1
    if l[1]>20 and l[1]<=40:
        return 2
    if l[1]>40 and l[1]<=60:
        return 3
    if l[1]>60 :
        return 4

def ConvertSex(l):
    if l[2]=="Male":
        return 1
    if l[2]=="Female":
        return 0

def ConvertEmabarked(l):
    if l[5]=="Cherbourg":
        return 0
    if l[5]=="Queenstown":
        return 1
    if l[5]=="Southampton":
        return 2

def ConvertTicket(l):
    if l[0]=="1st":
        return 1
    if l[0]=="2nd":
        return 2
    if l[0]=="3rd":
        return 3






def ConvertData(l):
    data = [ConvertTicket(l),ConvertAge(l),ConvertSex(l),l[3],l[4],ConvertEmabarked(l)]
    return data

def ConvertClass(x):
    if x==[0] :
        return "Survived"
    if x==[1]:
        return "Did not Survive"



