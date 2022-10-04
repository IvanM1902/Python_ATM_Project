# Object oriented programming Assignment
# Ivan Medved   C20338661
# Python 3.9: Bank Management System

import random
# I used csv files instead of txt files as it was easier for me to understand the concept of this, and to read, and write
# Here is a link from where I learned that: https://www.youtube.com/watch?v=q5uM4VKywbA
import csv
from datetime import date, datetime

# Customer class has all details about customer
class Customer(object):

    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age

    def __str__(self):
        return "{},{},{}".format(self.username,self.password,self.age)

    def age(self):

        return "{}".format(self.age)

    def username(self):

        return "{}".format(self.username)

# Account class has all info about specific account
class Account(object):

    def __init__(self, accNum, iban, funds, type):
        self.accNum = accNum
        self.iban = iban
        self.funds = funds
        self.type = type

    def __str__(self):
        return "Account INFO:\n\nUsername:{}\nType:{} \nIBAN:{}\nFunds:{}\naccNum:{}".format(customer.username,self.type,self.iban,self.funds,self.accNum)

    # Withdraw function deletes funds from users account, also has error checking for specific things
    # Error checking if user is trying to withdraw more money than they are allowed
    def withdraw(self, amount):
        if amount <= 0:
            print("You can only withdraw a positive value")
            return
        balance = self.funds - amount
        flag = False

        if self.type == "Savings":
            withdrawDate()

        if balance < 0 and self.type == "Savings":
            print("Insufficient funds")
            menu3()
            flag = True

        if balance < -5000 and self.type == "Checkings":
            print("Insufficient funds")
            menu3()
            flag = True

        if flag == False:
            self.funds -= amount
            Type = "Withdraw"
            editAccount()
            acctransaction(Type, amount)

    # Deposit function in account class, checks if amount entered is bigger than 0
    # If that is true adds money to account
    def deposit(self, amount):
        if amount <= 0:
            print("You can only deposit a positive value")
            return

        self.funds += amount
        Type = "Deposit"
        editAccount()
        acctransaction(Type, amount)

    # Transfer function in account class checks if amount entered is greater than 0
    # If yes decrements value of users account, and adds funds to account that money was transfered to
    # Error checking if user is trying to transfer more money than they are allowed
    def transfer(self, amount, iban):
        if amount <= 0:
            print("You can only transfer a positive value")
            return
        balance = self.funds - amount
        flag = False
        if self.type == "Savings":
            transferDate()

        if balance < 0 and self.type == "Savings":
            print("Insufficient funds")
            menu3()
            flag = True

        if balance < -5000 and self.type == "Checkings":
            print("Insufficient funds")
            menu3()
            flag = True

        if flag == False:
            self.funds -= amount
            Type = "Transfer"
            editAccount()
            acctransaction(Type, amount)
            transfermoney(iban, amount)

    # Function delete called when user picks option to delete account
    def delete(self):
        deleteacc()

    # Function lists all transactions made by users account
    def listtransactions(self):
        file = open('accountsTransactions.csv', 'r')
        Reader = csv.reader(file)
        num = self.accNum
        print("Transaction type\t Transaction amount\t Transaction Date")
        for row in Reader:
            if row[1] == str(num):
                print(row[2],"\t\t\t\t",row[3],"\t\t\t\t",row[4])


# Create customer function called when registration option is chosen, has error checking for age as it must be integer
# Also checks if password is longer than 6 characters, and if age is over 14
def createCustomer():
    db = open("customers.csv","r")
    print("#####     Registration     #####")
    id = incrementIDCustomer()
    Username = input("Please enter your username:")
    Password = input("Please enter your password:")
    while True:
        try:
            Age = int(input("Please enter your age: "))
            break
        except Exception:
            print("Please input an integer for your age!")
    data = [id,Username,Password,Age]

    usernamecheck(Username)
    if Password == "" or Username == "":
        print("You can't leave fields empty")
        menu1()
    elif len(Password) < 6:
        print("Your password has to be at least 6 characters long.")
        menu1()
    elif Age < 14:
        print("You are too young to opet account in our bank")
        menu1()
    else:
        with open('customers.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write multiple rows
            writer.writerow(data)
        print("You are successfully registered!")

# Login function called when option 1 from menu 1 is chosen, i.e. login option
# Gives user an option to login, has error checking if value was left empty, also gives an appropriate message if wrong username or password is entered
def login():
    print("#####     Login     #####")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == "" or password == "":
        print("You can't leave anything empty!")
        login()
    else:
        with open('customers.csv', 'r') as f:
            reader = csv.reader(f, delimiter =",")
            header = next(reader)
            for row in reader:
                user = row[1]
                code = row[2]
                age = row[3]
                if (user == username) and (code == password):
                    global customer
                    customer = Customer(user,code,int(age))
                    print("You are succesfully logged in!!")
                    menu2()
            else:
                print("User with this username or password does not exist!")

# Createaccount function called when user choose an option to create new account, it gives appropriate messages
# Has error checking for entering an integer, and also if user entered either Checkings or Savings option
def createAccount():
    print("#####     Account Creation     #####")
    db = open('accounts.csv', 'r')
    while True:
        try:
            acc_num = int(input("Please enter your account number: "))
            break
        except Exception:
            print("Please input an integer for account number!")
    acctype = input("Please enter account type you want to open (Checkings OR Savings):")
    iban = random.randint(1000000000, 9999999999)
    funds = 0
    name = customer.username
    data = [name, acc_num, acctype, iban, funds]
    existingnum(acc_num)
    if acctype == "Savings" or acctype == "Checkings":
        if (acctype == "Savings") and (customer.age < 14):
            print("You are too young to open savings account!")
        elif (acctype == "Checkings") and (customer.age < 18):
            print("You are too young to open Checkings account!")
        else:
            with open('accounts.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)

                # write multiple rows
                writer.writerow(data)
            print("Account succesfully created!")

    else:
        print("You have chosen wrong account type! Please enter Savings or Checking!")

#This function is called when user picks an option to choose account, it gives user an appropriate message
#Also has error checking if either value was left empty or account with that number is not existing for that user
def chooseAccount():
    acc_num = input("Please enter number of account you want to access:")
    username = customer.username
    if acc_num == "":
        print("You can't leave input empty!")
        chooseAccount()
    else:
        with open('accounts.csv', 'r') as f:
            reader = csv.reader(f, delimiter =",")
            header = next(reader)
            for row in reader:
                user = row[0]
                num = row[1]
                type = row[2]
                IBAN = row[3]
                Funds = row[4]
                if (user == username) and (acc_num == num):
                    global account
                    account = Account(int(num),int(IBAN),int(Funds),type)
                    menu3()
            else:
                print("You don't have account with that account number!")

#This function is called if either withdraw, deposit or transfer was made to change the value of funds to new value
def editAccount():
    # Changing value in the file
    file = open('accounts.csv', 'r')
    Reader = csv.reader(file)
    L = []
    accnum = account.accNum
    newFunds = account.funds
    for row in Reader:
        if row[1] == str(accnum):
            row[4] = str(newFunds)
            print("success")
        L.append(row)
    file.close()

    file = open('accounts.csv', 'w+', newline='')
    Writer = csv.writer(file)
    Writer.writerows(L)
    file.seek(0)

#This function is called either when withdraw, deposit or transfer is made, and it adds transaction to the document accountstransactions
def acctransaction(Type,amount):
    id = incrementIDTransaction()
    accnum = str(account.accNum)
    type = Type
    Amount = str(amount)
    today = date.today()
    d1 = today.strftime("%Y,%m,%d")
    data = [id,accnum,type,Amount,d1]

    with open('accountsTransactions.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write multiple rows
        writer.writerow(data)

#This function is called when money is transfered, i.e. it changes the funds of the account to which money was transfered
def transfermoney(iban, amount):
    # Changing value in the file
    file = open('accounts.csv', 'r')
    Reader = csv.reader(file)
    L = []
    Iban = iban
    Amount = amount
    for row in Reader:
        if row[3] == str(Iban):
            oldFunds = int(row[4])
            newFunds = Amount + oldFunds
            row[4] = str(newFunds)
            print("success")
        L.append(row)
    file.close()

    file = open('accounts.csv', 'w+', newline='')
    Writer = csv.writer(file)
    Writer.writerows(L)
    file.seek(0)

#This function is called if user confirms to delete account, it deletes user account from the file
def deleteacc():
    file = open('accounts.csv', 'r')
    Reader = csv.reader(file)
    L = []
    accnum = account.accNum
    for row in Reader:
        if row[1] == str(accnum):
            print("success")
        else:
            L.append(row)
    file.close()

    file = open('accounts.csv', 'w+', newline='')
    Writer = csv.writer(file)
    Writer.writerows(L)
    file.seek(0)

#This function is called when user wants to transfer money, i.e. checks entered iban
#If IBAN is same as users account, prints appopriate message, also if there is no account with that iban in the bank prints appropriate message
def transfercheck(iban):
    file = open('accounts.csv', 'r')
    Reader = csv.reader(file)
    Iban = iban
    if iban == str(account.iban):
        print("You can't transfer money to same account from which you are trying to transfer!")
        menu3()
    for row in Reader:
        if row[3] == str(Iban):
            return

    print("Account with that Iban doesn't exist please try again!")
    menu3()
    file.close()

#This function is called when user wants to create new account and checks if the entered account number is already existing
#If there is an existing account with that number in bank gives an appropriate message
def existingnum(acc_num):
    file = open('accounts.csv', 'r')
    Reader = csv.reader(file)
    number = acc_num
    Check = 0
    for row in Reader:
        if row[1] == str(number):
            print("Account with this number already exists!")
            Check = 1
    if Check == 1:
        menu2()
        file.close()

#This function is called when user want's to register, and it checks if user with the same username already exists in database
def usernamecheck(Username):
    file = open('customers.csv', 'r')
    Reader = csv.reader(file)
    user = Username
    Check = 0
    for row in Reader:
        if row[1] == str(user):
            print("User with that username already exists")
            Check = 1
    if Check == 1:
        menu1()
        file.close()

#This function is called when user picks an option to list all their accounts, and print's list of account for user
#if no accounts found prints appropriate message
def listAccounts():
    file = open('accounts.csv', 'r')
    Reader = csv.reader(file)
    Check = 0
    print(customer.username, "'s accounts:\n")
    for row in Reader:
        if row[0] == customer.username:
            print("AccNum:{}, AccType:{}, IBAN: {}, Funds:{}".format(row[1],row[2],row[3],row[4]))
            Check=1
    if Check == 0:
        print("No accounts found!")
        menu2()

#This function is called when some transaction is made and ID is added to transaction, this function auto increments ID
def incrementIDTransaction():
    file = open('accountsTransactions.csv', 'r')
    Reader = csv.reader(file)
    header = next(Reader)
    id = 0
    for row in Reader:
        id = row[0]
    file.close()
    ID = int(id)
    ID += 1
    FinalID = str(ID)
    return FinalID

#This function is called when new user wants to register and auto increments ID of new user added to the database
def incrementIDCustomer():
    file = open('customers.csv', 'r')
    Reader = csv.reader(file)
    header = next(Reader)
    id = 0
    for row in Reader:
        id = row[0]
    file.close()
    ID = int(id)
    ID += 1
    FinalID = str(ID)
    return FinalID

# This function is called if withdraw is made from savings account to check if user has made withdraw in last 30 days
def withdrawDate():
    file = open('accountsTransactions.csv', 'r')
    Reader = csv.reader(file)
    header = next(Reader)
    Num = account.accNum
    today = datetime.today()
    olddate = ""
    difference = 0
    Check = False
    for row in Reader:
        if row[1] == str(Num) and row[2] == "Withdraw":
            olddate = row[4]
            Check = True
    file.close()

    if Check == True:
        transdate = datetime.strptime(olddate, '%Y,%m,%d')
        difference = (today - transdate).days

    if difference < 30 and Check == True:
        print("You can't make this withdraw, as you already had a withdraw from this account in last 30 days!")
        menu3()

# This function is called if transfer is being made by savings account to check if user has already made transfer in last 30 days
def transferDate():
    file = open('accountsTransactions.csv', 'r')
    Reader = csv.reader(file)
    header = next(Reader)
    Num = account.accNum
    today = datetime.today()
    olddate = ""
    difference = 0
    Check = False
    for row in Reader:
        if row[1] == str(Num) and row[2] == "Transfer":
            olddate = row[4]
            Check = True
    file.close()

    if Check == True:
        transdate = datetime.strptime(olddate, '%Y,%m,%d')
        difference = (today - transdate).days

    if difference < 30 and Check == True:
        print("You can't make this transfer, as you already had a transfer from this account in last 30 days!")
        menu3()





#menu1 is a function which runs main menu and gives user an option to register and login
def menu1():
    ch = ''
    while ch !='3':
        print("MAIN MENU")
        print("1.Login")
        print("2.Register")
        print("3.Exit")
        print("Please select option (1-3)")

        ch = input()

        #if option 1.Login chosen, login() function is called
        if ch == '1':
            login()

        # if option 2.Register chosen, createCustomer() function is called
        elif ch == '2':
            createCustomer()

        #if option 3.Exit chosen, program ends
        elif ch == '3':
            print("Bye Bye")
            exit()
        else:
            print("Invalid input")

#menu 2 displays second menu to user, i.e. the menu when user is logged in
def menu2():
    ch = ''
    while ch !='4':
        print("CUSTOMER MENU")
        print("1.Create new account")
        print("2.Choose Account")
        print("3.List all my accounts")
        print("4.Logout")
        print("Please select option (1-4)")

        ch = input()

        #option 1 allows user to create new account
        if ch == '1':
            createAccount()

        # option 2 allows user to choose one of their accounts and progress to menu 3
        elif ch == '2':
            chooseAccount()

        # option 3 displays the list of all accounts logged in user has
        elif ch == '3':
            listAccounts()

        # option 4 allows user to log out
        elif ch == '4':
            print("Successfully logged out")
            ch = ''
            menu1()
        else:
            print("Invalid input")

#menu 3 function, displays third menu in program, i.e. menu where user has options to do something with their account
def menu3():
    ch = ''
    while ch !='7':
        print("\n1.Check account INFO")
        print("2.View all transactions made on this account")
        print("3.Deposit money to account")
        print("4.Withdraw from account")
        print("5.Transfer money")
        print("6.Delete Account")
        print("7.Go back to customer menu")
        print("Please select option (1-7)")

        ch = input()

        #option 1 displays account info to the user
        if ch == '1':
            print(account.__str__())
            menu3()

        if ch == '2':
            account.listtransactions()

        #option 3 allows user t deposit money to account
        elif ch == '3':
            #error checking if user has input an integer
            try:
                amount = int(input("Please enter amount you want to deposit:"))
            except ValueError:
                print('\nYou did not enter a valid integer')
                menu3()
            account.deposit(amount)

        #option 4 allows user to withdraw money from account
        elif ch == '4':
            # error checking if user has input an integer
            try:
                amount = int(input("Please enter amount you want to withdraw:"))
            except ValueError:
                print('\nYou did not enter a valid integer')
                menu3()
            account.withdraw(amount)

        #option 5 allows user to transfer money to different account
        elif ch == '5':
            iban = input("Please enter IBAN to which you want to transfer money:")
            #transfercheck function called to do error checking on entered iban
            transfercheck(iban)
            # error checking if user has input an integer
            try:
                amount = int(input("Please enter amount you want to transfer:"))
            except ValueError:
                print('\nYou did not enter a valid integer')
                menu3()
            account.transfer(amount,iban)

        # option 6 allows user to delete account, also has a confirmation menu
        elif ch == '6':
            ch = ''
            while ch != 2:
                print("Are you sure you want to delete this account?")
                print(account.__str__())
                print("\n1.Yes, Delete my account")
                print("2.No, don't delete my account")
                print("Please select option (1 or 2)")
                ch = input()
                if ch == '1':
                    account.delete()
                    menu2()
                elif ch == '2':
                    menu3()
                else:
                    print("Invalid input")

        #option 7 allows user to go back to user menu where they can choose different account
        elif ch == '7':
            menu2()
        else:
            print("Invalid Input")


#Program starts
menu1() # Main menu is called




