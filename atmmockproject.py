from sys import exit
import time
import random

# Time function to record user login time
currentDateAndTime = time.ctime()

# Mutable list of users, Account numbers are the KEYS, list holds the VALUES: Surname, firstname, PIN and balance respectively
userDatabase = {
    2028900090: ["Zuri", "Seyi", 1122, 11212],
    2063517879: ["Zuri", "Mike", 2233],
    2060195101: ["Zuri", "Love", 3344],
}


def main():

    print(f"Welcome User...")
    time.sleep(1)
    print(f"What transaction would you like to carry out?")
    time.sleep(1)

    # Asks user for transaction option
    choice = int(
        input(f"1. Cash Transfer\n2. Withdrawal\n3. Cash Deposit\n4. Check Balance\n")
    )

    # Checks to see is choice is valid
    if not choice in range(1, 5):
        exit("Invalid option, please try again!")

    # Figures out if user is a pre-existing user or new one and then proceeds to create account or log user in
    isAccountHolder = int(input("\nDo you have a bank account?\n1. Yes\n2. No\n"))

    # Throws an error and quits when user selects invalid option
    if not isAccountHolder in range(1, 3):
        exit("Invalid option, please try again!")

    # Felt this was useful cos some new users might not be willing to create an account
    if isAccountHolder == 2:
        regOrNot = int(input("Would you like to register an account?\n1. Yes\n2. No\n"))

        # Throws an error if option selected is invalid
        if not regOrNot in range(1, 3):
            exit("Invalid selection! Please retry again...Thank you!")

        # Registers user if option is selected
        elif regOrNot == 1:
            lastName, firstName, pin, accountNo = register()
            userDatabase[accountNo] = [lastName, firstName, pin]
            name, accountNo = login()
        else:
            logout()

    # Logs user in if option is selected
    else:
        name, accountNo = login()
        print(f"Welcome {name}")

    # If blocks to determine user transaction
    if choice == 1:
        cashTransfer(accountNo)
    elif choice == 2:
        print(f"Your new account balance is NGN{withdrawal(accountNo)}")
    elif choice == 3:
        print(f"Your new account balance is NGN{cashDeposit(accountNo)}")
    else:
        print(f"Your account balance is NGN{checkBalance(accountNo)}")

    # End transaction or not...
    restart = int(input("End transaction?\n1. Yes\n2. No\n"))

    if not restart in range(1, 3):
        exit("Invalid selection...Thank you for banking with us!")

    if restart == 1:
        logout()
    else:
        main()


def login():

    userAccountNo = int(input("\nPlease login with your 10-digit account number:\n"))
    # pin = int(input("Verify your 4-digit PIN: "))

    tries = 3

    for key, value in userDatabase.items():
        if key == userAccountNo:
            # if value[2] == pin:
            #     print(f"\n****** Login *******\n{currentDateAndTime}\n")
            #     return value[1], userAccountNo
            # else:
            #     exit("Invalid PIN")

            # Try Except block catches user input errors
            while True:
                if tries == 0:
                    exit("Invalid PIN\nMaximum of 3 tries exceeded!")
                try:
                    pin = int(input("Verify your 4-digit PIN: "))
                except ValueError:
                    tries -= 1
                    continue
                if value[2] != pin:
                    tries -= 1
                    print(f"Invalid PIN\nYou have {tries} tries left")
                    continue
                else:
                    print(f"\n****** Login *******\n{currentDateAndTime}\n")
                    return value[1], userAccountNo
    exit("Account Number does not exist\nPlease try again later!")


def register():

    print("\n****** Account Registration *******\n")

    userName = list()
    userName.append(input("What is your Last Name?\n"))
    userName.append(input("What is your First Name?\n"))

    val = 4
    while True:
        try:
            if val == 0:
                exit("Too many tries!")
            userPin = int(input("Please create a 4-digit pin\n"))
        except ValueError:
            val -= 1
            print(f"Invalid argument passed\nYou have {val} tries left.")
            continue
        if len(str(userPin)) != 4:
            val -= 1
            print(f"You have {val} tries left.\nPlease use 4 digits")
            continue
        else:
            if userPin == int(input("Verify PIN: ")):
                break
            else:
                exit("PINs provided do not match\nPlease try again later")

    userAccountNo = generateAccountNo()

    print(
        f"Congratulations, {userName[1]}\nYour new Account Number is: {userAccountNo}\nUse this to login along with your PIN"
    )

    return userName[0], userName[1], userPin, userAccountNo


def generateAccountNo():
    return int("20" + str(random.randrange(11111111, 99999999)))


def cashTransfer(accountNo):
    profile1 = userDatabase[accountNo]

    try:
        str(profile1[3])
    except IndexError:
        profile1.append(10000)

    destinationAccount = int(input("Please enter destination account: "))

    if destinationAccount == accountNo:
        exit("\nInvalid Operation\nYou cannot transfer to your account")

    if not destinationAccount in userDatabase.keys():
        exit("Invalid Account Number")

    profile2 = userDatabase[destinationAccount]
    amount = int(input("Kindly specify amount to transfer in NGN: "))

    if amount > profile1[3]:
        exit("Insufficient funds!\nKindly deposit and then try again!")

    try:
        profile2[3] += amount
    except IndexError:
        profile2.append(10000 + amount)

    profile1[3] -= amount
    print(f"Traansaction successful\nNew account balance is NGN{profile1[3]}")


def withdrawal(accountNo):

    profile = userDatabase[accountNo]
    try:
        str(profile[3])
    except IndexError:
        profile.append(10000)

    amount = int(input("Input amount to withdraw in NGN: "))

    if amount > profile[3]:
        exit("Insufficient funds!\nKindly deposit and then try again!")

    profile[3] -= amount
    return profile[3]


def cashDeposit(accountNo):

    profile = userDatabase[accountNo]

    try:
        str(profile[3])
    except IndexError:
        profile.append(10000)

    amount = int(input("Kindly specify amount to deposit in NGN: "))

    profile[3] += amount
    return profile[3]


def checkBalance(accountNo):

    profile = userDatabase[accountNo]

    try:
        return profile[3]
    except IndexError:
        profile.append(10000)
    return profile[3]


def logout():
    exit("Thank you for your patronage!\n\n****** Logout *******")


if __name__ == "__main__":
    main()

####################### PREVIOUS CODE ###########################

# # Requests users name
# name = input("What is your Name?\n")

# # Prepopulated list of allowed users
# allowedUsers = ["Seyi", "Mike", "Love"]

# # Passwords assigned to allowed users
# allowedPasswords = ["passwordSeyi", "passwordMike", "passwordLove"]

# # Evaluates is in the list of names
# if not name in allowedUsers:
#     sys.exit("Name not found, please try again")

# # Indexes users input
# userId = allowedUsers.index(name)
# passwordCount = 0

# # Checks for indexed users password in the allowed passwords
# # While loop allows for only three trials on the user's password using passwordCount
# while True:
#     password = input("Your Password:\n")

#     if not password == allowedPasswords[userId]:
#         passwordCount += 1
#         if passwordCount == 3:
#             sys.exit("Password limit reached\nPlease try again later")
#         continue
#     else:
#         break

# # Assigns the local date and time to a variable
# currentDateAndTime = time.ctime()

# # Prints the local date and time
# print(f"\n{currentDateAndTime}\n\nWelcome {name},\nThese are the available options:")

# # Displays options for user to select
# print("1. Withdrawal\n2. Cash Deposit\n3. Lodge a Complaint\n")

# # Requests input from user
# userInput = int(input("Please select an option:\n"))

# # Checks to user input and asks corresponding question
# if userInput == 1:
#     input("How much would you like to withdraw?\n")
#     sys.exit("Please take your cash")
# elif userInput == 2:
#     deposit = input("How much would you like to deposit?\n")
#     sys.exit(f"Current balance = {deposit}")
# elif userInput == 3:
#     complaint = input("What issue would you like to report?\n")
#     sys.exit("Thank you for contacting us")
# else:
#     sys.exit("Invalid Option selected, please try again later")