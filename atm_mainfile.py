# The code implements a simple ATM system that allows users to 
# check their balance, withdraw and deposit cash, change their PIN, and view a mini statement of recent transactions.
#  It includes input validation and limits the number of incorrect PIN attempts.

# now we will initialize the variables
name="Devansh khemka"
# the attempts increase with wrong pin attempts
attempts=0

# The list store the transactions
transactions = []

# initial balance which can change with withdraw and deposit
balance=10000

# initial pin which can be changed
pinlist = ['1234']

# welcome message and taking name input

print("Welcome to ATM")
print("----------------")
# taking input of the pin
pin=input("Enter the four digit pin: ")

# checking the pin with 3 attempts
for i in range(3):

    if pin == pinlist[0]:

        # printing the correct print message
        print("\nCorrect pin")

        # prints the number of stars equal to the length of the name except the last character
        print("\nwelcome,", name)

        # if the pin is correct we will break the loop
        break

    elif len(str(pin)) != 4:

        # if the elif is true we will print this message
        print("\nIncorrect pin,enter 4 digits only:")
        pin = input()

        # and we will increase the attempts by 1
        attempts += 1

        # and if the the attempts reach 3 we will print the account locked message and quit
        if attempts == 3:
            print("\nToo many wrong attempts. Account locked.")
            quit()

    elif pin.isdigit() == False:

        # if the elif is true we will print this message
        print("\nIncorrect pin, enter digits only:")
        pin = input()

        # and we will increase the attempts by 1
        attempts += 1

        # and if the the attempts reach 3 we will print the account locked message and quit
        if attempts == 3:
            print("\nToo many wrong attempts. Account locked.")
            quit()
    else:

        # this else is for when the pin is four digit and contains only digits but is incorrect
        print("\nIncorrect pin, try again:")
        pin = input()

        # and we will increase the attempts by 1
        attempts += 1

        # and if the the attempts reach 3 we will print the account locked message and quit
        if attempts == 3:
            print("\nToo many wrong attempts. Account locked.")
            quit()

# gives the main menu to choose
# the while loop until the user exits
# for this we use the true condition 

while True:
    # prints a simple main main and option to choose
    print("\n--- Main Menu ---")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Change PIN")
    print("5. Mini Statement")
    print("6. Exit")

    # takes input of the choice as a string
    choice = input("Enter your choice (1-6): ")

    # check balance
    if choice == '1':
        # prints the current balance
        print(f"\nYour current balance is ₹{balance}")

    # withdraw cash
    elif choice == '2':

        withdrawamount = input("Enter amount to withdraw: ₹")

        # checks if the withdraw amount is a valid number, if the amount is digit or not
        if withdrawamount.isdigit()==False:
            print("\nPlease enter a valid number.")

        else:
            amount = int(withdrawamount)

            # the condition to check if the amount is greater than zero and less than or equal to balance
            if amount <= 0:
                print("\nAmount must be greater than zero.")

            # if the amount is greater than the balance it will print insufficient balance
            elif amount > balance:
                print("\nInsufficient balance.")

            else:
                # the withdrawn amount is subtracted from the balance
                balance -= amount

                # and the transaction is added to the transactions list with a '-' sign
                transactions.append(f"-{amount} Withdrawal")


                print("\nWithdrawal successful. Please collect your cash.")

                # asks if the user wants to check balance after withdrawal
                print("\nWould you like to check your balance? (yes/no)")

                # it takes input and converts it to lowercase
                check_balance = input().lower()

                # if the user inputs yes it will print the current balance
                if check_balance == 'yes':
                    print(f"\nYour current balance is ₹{balance}")
                else:
                    pass

    # deposit cash
    elif choice == '3':
        depositamount = input("Enter amount to deposit: ₹")

        # checks if the deposit amount is a valid number, if the amount is digit or not
        if depositamount.isdigit()==False:
            print("\nPlease enter a valid number.")

        else:
            amount = int(depositamount)

            # the condition to check if the amount is greater than zero
            if amount <= 0:
                print("\nAmount must be greater than zero.")
            else:
                # the deposited amount is added to the balance
                balance += amount

                # and the transaction is added to the transactions list with a '+' sign
                transactions.append(f"+{amount} Deposit")

                print("\nDeposit successful.")

                # asks if the user wants to check balance after withdrawal
                print("\nWould you like to check your balance? (yes/no)")

                # it takes input and converts it to lowercase
                check_balance = input().lower()

                # if the user inputs yes it will print the current balance
                if check_balance == 'yes':
                    print(f"\nYour current balance is ₹{balance}")
                else:
                    pass

    # change pin
    elif choice == '4':
        currentPin = input("Enter your current PIN: ")

        # checks if the current pin entered is correct
        if currentPin != pinlist[0]:
            print("\nIncorrect current PIN. PIN not changed.")
        else:
            # taking input of the new pin
            newpin1 = input("Enter new 4-digit PIN: ")

            # taking input to confirm the new pin
            newpin2 = input("Confirm new PIN: ")

            # checks if the new pin is contains only digits and is of 4 digits
            if newpin1.isdigit()==False or len(newpin1) != 4:
                print("\nPIN must be 4 digits.")

            # checks if the new pin and confirm pin match
            elif newpin1 != newpin2:
                print("\nPINs do not match.")

            else:
                # using the pod we remove the old pin 
                pinlist.pop(0)

                # and append the new pin to the list
                pinlist.append(newpin1)
                print("\nPIN updated successfully.")

    # mini statement
    elif choice == '5':

        # check if there are any transactions
        # if not it will print the no transactions message
        if len(transactions) == 0:
            print("\nNo transactions yet.")

        # else it will print the last 5 transactions
        else:
            print("\nYour balance is ₹",balance)
            print("\nLast transactions:")


            # to print the last 5 transactions we use slicing and a for loop
            for transaction in transactions[-1:-6:-1]:
                print(transaction)
            # continue to menu after listing

    # exit
    elif choice == '6':
        print("\nThank you for using our ATM.")
        #the break statement is used to exit the while loop
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")

