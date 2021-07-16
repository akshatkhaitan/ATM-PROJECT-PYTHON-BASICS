import csv
from constants import *
from menu import *


pin = '0'
f = open('data.csv', 'r+', newline='')
reader = csv.reader(f)
writer = csv.writer(f)




class Account():
    def __init__(self, pin, current_balance, account_number):
        self.pin = pin
        self.current_balance = current_balance
        self.account_number = account_number

    def send_money(self, recipient):
        global f, reader,writer,pin 
        amount = input("Enter the amount to be transferred : ")
        self.withdraw_money(amount)
        f.seek(0)
        data = list(reader)
        for i in range(len(data)):
            if recipient == data[i][0]:
                data[i][2] = str(int(data[i][2]) + int(amount))
                break
        f.truncate(0)
        f.close()
        f = open('data.csv', 'r+', newline='')
        reader = csv.reader(f)
        writer = csv.writer(f)
        writer.writerows(data)

    def deposit_money(self, amount):
        global f, reader,writer,pin 
        f.seek(0)
        data = list(reader)
        for i in range(len(data)):
            if self.pin == data[i][1]:
                data[i][2] = str(int(self.current_balance) + int(amount))
                break
        f.truncate(0)
        f.close()
        f = open('data.csv', 'r+', newline='')
        reader = csv.reader(f)
        writer = csv.writer(f)
        writer.writerows(data)

    def withdraw_money(self, amount):
        global f, reader,writer,pin 
        f.seek(0)
        data = list(reader)
        for i in range(len(data)):
            if self.pin == data[i][1]:
                if (data[i][2] < amount):
                    print("LOW BALANCE !! ABORTING TRANSACTION\n")
                    start()
                data[i][2] = str(int(self.current_balance) - int(amount))
                break
        f.truncate(0)
        f.close()
        f = open('data.csv', 'r+', newline='')
        reader = csv.reader(f)
        writer = csv.writer(f)
        writer.writerows(data)

    def display(self):
        print(f"Account balane is : {self.current_balance}")



def validate_pin():
    global f, reader, writer, pin 
    f.seek(0)
    pin = input("Enter your pin to proceed with the transaction : ")
    flag = False
    for data in reader:
        if data[1] == pin:
            flag = True
            break
    if not flag:
        print("Invalid Pin! Aborting Transaction \n Try Again!!\n\n")
        return flag
    else:
        return flag


def getANByPin():
    global f, reader,writer,pin 
    f.seek(0)
    for row in reader:
        if (row[1] == pin):
            return row[0]


def getBalanceByPin():
    global f, reader,writer,pin 
    f.seek(0)
    for data in reader:
        if data[1] == pin:
            return data[2]

def getBalanceByAN(an):
    global f, reader,writer,pin 
    f.seek(0)
    for data in reader:
        if data[0] == an:
            return True
    return False


def checkPin(pin):
    global f, reader,writer
    f.seek(0)
    for data in reader:
        if data[1] == pin:
            return False
    return True


def start():
    global f, reader,writer,pin     
    display_menu()
    choice = int(input())
    if(choice == 6):
        print("Thank You For Visiting . See you Soon!!\n")
        f.close()
        exit(0)
    elif(choice < 1 or choice >= 7):
        print("No Such Option Exists. Try Again\n")
        start()

    if choice in range(1, 6):
        if(choice == NEW_ACCOUNT):
            pin = input("Enter Your New Pin : ")
            if not checkPin(pin):
                print("The given Pin is not available!! Please Try again!!\n")
                start()
            f.seek(0)
            data = list(reader)
            for row in data:
                ac_no = str(int(row[0]) + 1)
            writer.writerow([ac_no, pin, '0'])
            print("ACCOUNT CREATED SUCCESSFULLY!! PROCEED TO ADD MONEY")
            start()

        else:
            if validate_pin():
                if(choice == SEND_MONEY):
                    an = getANByPin()
                    balance = getBalanceByPin()
                    ac = Account(pin, balance, an)
                    an = input("Enter the account Number of the recepient : ")
                    if getBalanceByAN(an):
                        ac.send_money(an)
                        start()
                    else:
                        print(
                            "No Such Account Number Exists!! Aborting Transaction !! \n")
                        start()
                if (choice == DISPLAY_BALANCE):
                    an = getANByPin()
                    balance = getBalanceByPin()
                    ac = Account(pin, balance, an)
                    ac.display()
                    print("CURRENT BALANCE DISPALYED SUCCESSFULLY\n\n")
                    start()
                if (choice == DEPOSIT):
                    an = getANByPin()
                    balance = getBalanceByPin()
                    ac = Account(pin, balance, an)
                    amount = input(
                        "Enter the amount of money you want to deposit : ")
                    ac.deposit_money(amount)
                    print("MONEY DEPOSITED \n\n")
                    start()
                if (choice == WITHDRAW):
                    an = getANByPin()
                    balance = getBalanceByPin()
                    ac = Account(pin, balance, an)
                    amount = input(
                        "Enter the amount of money you want to withdraw : ")
                    ac.withdraw_money(amount)
                    print("MONEY WITHDRAWN \n\n")
                    start()
            else:
                start()
start()


































enter()

