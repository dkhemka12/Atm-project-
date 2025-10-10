# The code implements a simple ATM system that allows users to 
# check their balance, withdraw and deposit cash, change their PIN, and view a mini statement of recent transactions.
#  It includes input validation and limits the number of incorrect PIN attempts.

# now we will initialize the variables

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

print("Please enter your name")

name=input()

print("Enter the four digit pin:")

# taking input of the pin
pin = input()
# checking the pin with 3 attempts
for i in range(3):

    if pin == pinlist[0]:

        # printing the correct print message
        print("Correct pin")

        # prints the number of stars equal to the length of the name except the last character
        print("welcome,", "*" * len(name)+ name[-1])

        # if the pin is correct we will break the loop
        break

    # this elif checks if the pin is of 4 digits
    elif len(str(pin)) != 4:

        # if the elif is true we will print this message
        print("Incorrect pin,enter 4 digits only:")
        pin = input()

        # and we will increase the attempts by 1
        attempts +=1

        # and if the the attempts reach 3 we will print the account locked message and quit
        if attempts == 3:
            print("Too many wrong attempts. Account locked.")
            quit()
    # this elif checks if the pin contains only digits
    elif pin.isdigit() == False:

        # if the elif is true we will print this message
        print("Incorrect pin, enter digits only:")
        pin = input()

        # and we will increase the attempts by 1
        attempts +=1

        # and if the the attempts reach 3 we will print the account locked message and quit
        if attempts == 3:
            print("Too many wrong attempts. Account locked.")
            quit()

    # this else is for when the pin is four digit and contains only digits but is incorrect
    else:
        print("Incorrect pin, try again:")
        pin = input()

        # and we will increase the attempts by 1
        attempts +=1

        # and if the the attempts reach 3 we will print the account locked message and quit
        if attempts == 3:
            print("Too many wrong attempts. Account locked.")
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
        print(f"Your current balance is ₹{balance}")

    # withdraw cash
    elif choice == '2':

        withdrawamount = input("Enter amount to withdraw: ₹")

        # checks if the withdraw amount is a valid number, if the amount is digit or not
        if withdrawamount.isdigit()==False:
            print("Please enter a valid number.")

        else:
            amount = int(withdrawamount)

            # the condition to check if the amount is greater than zero and less than or equal to balance
            if amount <= 0:
                print("Amount must be greater than zero.")

            # if the amount is greater than the balance it will print insufficient balance
            elif amount > balance:
                print("Insufficient balance.")

            
            else:
                # the withdrawn amount is subtracted from the balance
                balance -= amount

                # and the transaction is added to the transactions list with a '-' sign
                transactions.append(f"-{amount} Withdrawal")


                print("Withdrawal successful. Please collect your cash.")

                # asks if the user wants to check balance after withdrawal
                print("Would you like to check your balance? (yes/no)")

                # it takes input and converts it to lowercase
                check_balance = input().lower()

                # if the user inputs yes it will print the current balance
                if check_balance == 'yes':
                    print(f"Your current balance is ₹{balance}")

    # deposit cash
    elif choice == '3':
        depositamount = input("Enter amount to deposit: ₹")

        # checks if the deposit amount is a valid number, if the amount is digit or not
        if depositamount.isdigit()==False:
            print("Please enter a valid number.")
        else:
            amount = int(depositamount)

            # the condition to check if the amount is greater than zero
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                # the deposited amount is added to the balance
                balance += amount

                # and the transaction is added to the transactions list with a '+' sign
                transactions.append(f"+{amount} Deposit")

                print("Deposit successful.")

                # asks if the user wants to check balance after withdrawal
                print("Would you like to check your balance? (yes/no)")

                # it takes input and converts it to lowercase
                check_balance = input().lower()

                # if the user inputs yes it will print the current balance
                if check_balance == 'yes':
                    print(f"Your current balance is ₹{balance}")

    # change pin
    elif choice == '4':
        currentPin = input("Enter your current PIN: ")

        # checks if the current pin entered is correct
        if currentPin != pinlist[0]:
            print("Incorrect current PIN. PIN not changed.")
        else:
            # taking input of the new pin
            newpin1 = input("Enter new 4-digit PIN: ")

            # taking input to confirm the new pin
            newpin2 = input("Confirm new PIN: ")

            # checks if the new pin is contains only digits and is of 4 digits
            if newpin1.isdigit()==False or len(newpin1) != 4:
                print("PIN must be 4 digits.")

            # checks if the new pin and confirm pin match
            elif newpin1 != newpin2:
                print("PINs do not match.")

            else:
                # using the pod we remove the old pin 
                pinlist.pop(0)

                # and append the new pin to the list
                pinlist.append(newpin1)
                print("PIN updated successfully.")

    # mini statement
    elif choice == '5':

        # check if there are any transactions
        # if not it will print the no transactions message
        if len(transactions) == 0:
            print("No transactions yet.")

        # else it will print the last 5 transactions
        else:
            print("Last transactions:")

            # to print the last 5 transactions we use slicing and a for loop
            for transaction in transactions[-1:-6:-1]:
                print(transaction)

    # exit
    elif choice == '6':
        print("Thank you for using our ATM.")

        #the break statement is used to exit the while loop
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

