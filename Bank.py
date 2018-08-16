print("Coded by AndreTheApe")
print("")
#Introduce the user to the program, ask for their name,number,pin, and address
print("Hello user, Welcome to ApeJungle's Bank ATM")
print("")
print("Please begin with creating an account")
name=input("Enter your name: ")
phone=input("Enter your phone number: ")
address=input("Enter your address: ")
code=input("Please enter a pin to use as your passcode: ")
#Display User Info
print()
print("Your account summary is:")
print("Name:" + name)
print("Phone Number:" + phone)     
print("Address:" + address)
print("Pin Code:" + code)    
print()

#Entering Balance 
balance=float(input("Enter an amount to deposit into the account: "))
print()
print(name,", Thank you for creating an account.")
#User Controls
def printMenu():
    print()
    print("Please choose an option below:")
    print("""
    Enter d to Check your Balance
    Enter e to Deposit money into your Account
    Enter s to Withdraw money from your Account
    Enter u to Quit the Program """)
    print("")

def getTransaction():
    transaction=str(input("What would you like to do? "))
    return transaction

def withdraw(bal,amt):
    global balance
    balance=bal-amt
    if balance<0:
        balance=balance-10

def formatCurrency(amt):
    return "$%.2f" %amt


printMenu()
command=str(getTransaction())

while command!="u":
    if (command=="d"):
        print(name,"Your current balance is",formatCurrency(balance))
        printMenu()
        command=str(getTransaction())
    elif (command=="e"):
        amount=float(input("Amount to deposit? "))
        balance=balance+amount
        printMenu()
        command=str(getTransaction())
    elif (command=="s"):
        amount=float(input("Amount to withdraw? "))
        withdraw(balance,amount)
        printMenu()
        command=str(getTransaction())
    else:
        print("Incorrect command. Please try again.")
        printMenu()
        command=str(getTransaction())

print(name,"Goodbye! See you again soon. Always remember with ApeJungle you too can have the wealth of a Jungle King!")
