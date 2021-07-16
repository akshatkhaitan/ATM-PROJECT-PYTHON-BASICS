import main as m

def validate_pin():
    m.f.seek(0)
    pin = input("Enter your pin to proceed with the transaction : ")
    flag = False
    for data in m.reader:
        if data[1] == pin:
            flag = True
            break
    if not flag:
        print("Invalid Pin! Aborting Transaction \n Try Again!!\n\n")
        return flag
    else:
        return flag


def getANByPin():
    m.f.seek(0)
    for row in m.reader:
        if (row[1] == m.pin):
            return row[0]


def getBalanceByPin():
    m.f.seek(0)
    for data in m.reader:
        if data[1] == m.pin:
            return data[2]

def getBalanceByAN(an):
    m.f.seek(0)
    for data in m.reader:
        if data[0] == an:
            return True
    return False


def checkPin(pin):
    m.f.seek(0)
    for data in m.reader:
        if data[1] == pin:
            return False
    return True