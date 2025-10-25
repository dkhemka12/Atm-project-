# ===============================================
# ATM SYSTEM - COMPREHENSIVE BANKING SIMULATION
# ===============================================
# This program simulates a complete bank ATM system with the following features:
# - Multiple user account support with unique PINs
# - Balance checking functionality
# - Cash withdrawal with denomination breakdown
# - Cash deposit operations
# - PIN change capability with security verification
# - Mini statement showing last 5 transactions
# - Admin access mode for viewing all accounts and ATM cash inventory
# - Input validation and error handling throughout
# - Security features including PIN attempt limiting
# ===============================================
#
# PROGRAM STRUCTURE AND FLOW:
# 1. Data initialization (accounts, ATM cash inventory, variables)
# 2. User authentication via PIN entry (max 3 attempts)
# 3. Main menu presentation with 6 options
# 4. Transaction processing based on user selection
# 5. Session termination and exit
#
# SECURITY FEATURES:
# - Maximum 3 PIN entry attempts before account lockout
# - PIN verification required for PIN changes
# - Confirmation required for new PIN entry
# - Admin mode with special PIN (0000)
#
# USER EXPERIENCE ENHANCEMENTS:
# - Clear formatted output with visual separators
# - Optional balance checks after transactions
# - Optional receipt printing for transactions
# - Detailed transaction breakdown (withdrawal notes)
# ===============================================

# -----------------------------------------------
# DATA STRUCTURE: ACCOUNTS DICTIONARY
# -----------------------------------------------
# This dictionary stores all user account information
# Each account is keyed by its PIN and contains:
# - name: The account holder's full name
# - balance: Current account balance in rupees
# - transactions: List of all transactions during this session
# 
# NOTE: In a real banking system, this data would be stored
# in a secure database with encrypted PINs. For educational
# purposes, we use a simple dictionary structure.
# -----------------------------------------------
accounts = {
    "1234": {
        "name": "Devansh Khemka",  # Primary account holder
        "balance": 10000,  # Starting balance in rupees
        "transactions": []  # Empty list to store transaction history
        },
    "4321": {
        "name": "Anunay Sharma",  # Secondary account holder
        "balance": 8000,  # Starting balance in rupees
        "transactions": []  # Empty list to store transaction history
        },
    "1212": {
        "name": "Devi Shree",  # Third account holder
        "balance": 12000,  # Starting balance in rupees
        "transactions": []  # Empty list to store transaction history
        },
    "3434": {
        "name": "Aman Singh",  # Fourth account holder
        "balance": 5000,  # Starting balance in rupees
        "transactions": []  # Empty list to store transaction history
        },
    "1283": {
        "name": "Rohan Mehta",  # Fifth account holder
        "balance": 15000,  # Starting balance in rupees
        "transactions": []  # Empty list to store transaction history
        }
}

# -----------------------------------------------
# ATM CASH INVENTORY MANAGEMENT
# -----------------------------------------------
# This dictionary tracks the number of each denomination
# available in the ATM machine for dispensing cash
# Key: Note denomination (in rupees)
# Value: Number of notes available
# This is used during withdrawal to calculate note breakdown
# -----------------------------------------------
atmCash = {2000: 10, 500: 20, 200: 30, 100: 50}

# -----------------------------------------------
# SECURITY AND ATTEMPT TRACKING VARIABLES
# -----------------------------------------------
# maxAttempts: Maximum number of incorrect PIN entries allowed
# attempts: Current count of incorrect PIN attempts
# These variables work together to implement the security feature
# that locks the account after 3 failed PIN entry attempts
# -----------------------------------------------
maxAttempts = 3
attempts = 0

# -----------------------------------------------
# USER INTERFACE: WELCOME BANNER
# -----------------------------------------------
# The following section displays a formatted welcome message
# to the user when they start the ATM session. This creates
# a professional and user-friendly experience similar to
# real ATM machines used in banks.
#
# The banner includes:
# - XYZ Bank branding
# - Card insertion simulation messages
# - Security information about PIN attempts
# - Clear instructions for the user
# -----------------------------------------------
print("==================================================")
print("             WELCOME TO XYZ BANK ATM              ")
print("==================================================")
print("PLEASE INSERT YOUR ATM CARD...")
print("READING CARD... PLEASE WAIT...")
print("CARD DETECTED SUCCESSFULLY.")
print("--------------------------------------------------")
print("YOU HAVE 3 ATTEMPTS TO ENTER THE CORRECT PIN.")
print("PLEASE ENTER YOUR 4-DIGIT PIN CAREFULLY.\n")

# -----------------------------------------------
# AUTHENTICATION PHASE: PIN INPUT AND VERIFICATION
# -----------------------------------------------
# This section handles the critical security function of
# verifying the user's identity through PIN authentication.
#
# The PIN verification process includes:
# - Initial PIN entry prompt
# - Validation loop with maximum 3 attempts
# - Multiple validation checks (length, digit-only, correctness)
# - Account lockout mechanism after failed attempts
# - Admin mode access with special PIN
# - Loading correct account data upon successful authentication
#
# The 'pin' variable stores the user's entered PIN as a string
# to preserve leading zeros (e.g., "0123" vs 123)
# -----------------------------------------------
pin = input("ENTER YOUR 4-DIGIT PIN: ")

for i in range(3):
    # -----------------------------------------------
    # CASE 1: CORRECT PIN ENTERED
    # -----------------------------------------------
    # This is the success path where the entered PIN matches
    # one of the accounts in the system. When this happens:
    # 1. A success message is displayed to the user
    # 2. The user's name is retrieved and displayed in uppercase
    # 3. The account data is loaded into the 'account' variable
    # 4. The loop is broken to proceed to the main menu
    #
    # The 'in' operator checks if the PIN exists as a key
    # in the accounts dictionary, which is an efficient O(1) lookup
    # -----------------------------------------------
    if pin in accounts:
        print("\n==================================================")
        print("               PIN VERIFIED SUCCESSFULLY          ")
        print("==================================================")

        # Retrieve and display the account holder's name in uppercase
        # This provides a personalized greeting to make the user
        # feel welcomed and confirms they've accessed the right account
        print(f"WELCOME, {accounts[pin]['name'].upper()}")
        print("ACCESS GRANTED TO YOUR ACCOUNT.")
        print("--------------------------------------------------")

        # Load the complete account data (name, balance, transactions)
        # into the 'account' variable for easy access throughout
        # the session. This avoids repeated dictionary lookups.
        account = accounts[pin]  # Load the account details
        break  # Exit the PIN verification loop successfully

    # -----------------------------------------------
    # CASE 2: INVALID PIN LENGTH
    # -----------------------------------------------
    # This validation ensures the PIN has exactly 4 digits.
    # PINs must be 4 characters long for security standardization.
    #
    # Why this check matters:
    # - Prevents brute force attacks with variable-length PINs
    # - Maintains consistency with banking industry standards
    # - Provides clear feedback to users about format requirements
    #
    # The len(str(pin)) converts the PIN to a string (if not already)
    # and counts the characters. This handles cases where users
    # might enter numbers with leading zeros.
    # -----------------------------------------------
    elif len(str(pin)) != 4:
        print("\n--------------------------------------------------")
        print("PIN MUST BE 4 DIGITS ONLY. TRY AGAIN.")
        print("--------------------------------------------------")
        pin = input("RE-ENTER YOUR PIN: ")

        # Increment the failed attempt counter
        # This tracks how many times the user has entered an invalid PIN
        # After 3 attempts (when attempts reaches 2, since we start at 0),
        # the account will be locked for security purposes
        attempts += 1

        # Check if maximum attempts have been reached
        # We check for attempts == 2 because:
        # - Attempt 0: First try (failed)
        # - Attempt 1: Second try (failed)
        # - Attempt 2: Third and final try (failed) - LOCK ACCOUNT
        if attempts == 2:
            print("\n==================================================")
            print("ACCOUNT LOCKED DUE TO MULTIPLE INCORRECT ATTEMPTS.")
            print("PLEASE CONTACT YOUR BANK BRANCH.")
            print("==================================================")
            quit()  # Terminate the program to prevent further access

    # -----------------------------------------------
    # CASE 3: PIN CONTAINS NON-DIGIT CHARACTERS
    # -----------------------------------------------
    # This validation ensures the PIN contains only numeric digits.
    # PINs should never contain letters, symbols, or special characters.
    #
    # Security reasoning:
    # - Numeric-only PINs are industry standard
    # - Prevents injection attacks or malformed input
    # - Simplifies validation and comparison logic
    #
    # The isdigit() method returns True only if all characters
    # in the string are digits (0-9). The 'not' operator inverts
    # this to check for any non-digit characters.
    # -----------------------------------------------
    elif not pin.isdigit():
        print("\n--------------------------------------------------")
        print("PIN MUST CONTAIN DIGITS ONLY. TRY AGAIN.")
        print("--------------------------------------------------")
        pin = input("RE-ENTER YOUR PIN: ")

        # Increment the failed attempt counter
        # Same logic as Case 2 - tracking invalid PIN entries
        attempts += 1

        # Check if this was the final allowed attempt
        # Security lockout mechanism activates here
        if attempts == 2:
            print("\n==================================================")
            print("ACCOUNT LOCKED DUE TO MULTIPLE INCORRECT ATTEMPTS.")
            print("PLEASE CONTACT YOUR BANK BRANCH.")
            print("==================================================")
            quit()  # Terminate program to prevent unauthorized access

    # -----------------------------------------------
    # CASE 4: ADMIN MODE ACCESS
    # -----------------------------------------------
    # Special administrative access mode activated with PIN "0000"
    # This provides bank staff or system administrators with:
    # - View all customer accounts and balances
    # - Monitor ATM cash inventory levels
    # - System oversight without customer account access
    #
    # Security Note: In production systems, admin access would
    # require additional authentication (2FA, biometrics, etc.)
    # and would be logged for audit purposes.
    #
    # Admin capabilities:
    # 1. VIEW ALL ACCOUNTS - Display all registered accounts
    # 2. VIEW ATM CASH - Check denomination inventory
    # 3. EXIT ADMIN MENU - Return to main system
    # -----------------------------------------------
    elif pin == "0000":
        print("\n==================================================")
        print("               ADMIN ACCESS GRANTED               ")
        print("==================================================")
        print("WELCOME, ADMINISTRATOR.")
        print("==================================================")
        print("YOU CAN VIEW ALL ACCOUNTS AND ATM CASH INVENTORY.")
        
        # -----------------------------------------------
        # ADMIN MENU LOOP
        # -----------------------------------------------
        # Continuous loop for admin operations until exit is chosen
        # This allows administrators to perform multiple queries
        # in a single session without re-authentication
        # -----------------------------------------------
        while True:
            print("\n================ ADMIN MENU ==================")
            print("1. VIEW ALL ACCOUNTS")
            print("2. VIEW ATM CASH")
            print("3. EXIT ADMIN MENU")
            print("==============================================")
            choice = input("ENTER YOUR CHOICE: ")

            # -----------------------------------------------
            # ADMIN OPTION 1: VIEW ALL CUSTOMER ACCOUNTS
            # -----------------------------------------------
            # Displays a comprehensive list of all accounts in the system
            # Including account holder names and current balances
            # Useful for: Bank reconciliation, balance verification,
            # customer service inquiries, account monitoring
            # -----------------------------------------------
            if choice == '1':
                print("\n============== ACCOUNT LIST ==============")

                # Iterate through the accounts dictionary
                # The items() method returns key-value pairs:
                # - acc_pin: The account's PIN (dictionary key)
                # - acc_data: The account details (dictionary value)
                for acc_pin, acc_data in accounts.items():

                    # Display each account's holder name and current balance
                    # Format: "Name - BALANCE: ₹amount"
                    # This provides a clear, readable list of all accounts
                    print(f"{acc_data['name']} - BALANCE: ₹{acc_data['balance']}")
                print("==========================================")

            # -----------------------------------------------
            # ADMIN OPTION 2: VIEW ATM CASH INVENTORY
            # -----------------------------------------------
            # Displays the current stock of each currency denomination
            # Critical for:
            # - Ensuring adequate cash availability
            # - Planning cash replenishment schedules
            # - Monitoring denomination distribution
            # - Preventing cash-out situations
            # -----------------------------------------------
            elif choice == '2':
                print("\n================ ATM CASH =================")
                # Iterate through the cash inventory dictionary
                # note: Denomination value (2000, 500, 200, 100)
                # count: Number of notes of that denomination
                for note, count in atmCash.items():
                    print(f"₹{note}: {count} notes")
                print("===========================================")

            # Admin option 3: Exit admin menu
            elif choice == '3':
                print("\nEXITING ADMIN MENU...")
                print("==================================================")
                quit()

            else:
                print("\nINVALID CHOICE. TRY AGAIN.")

    # Case 5: Incorrect PIN entered
    else:
        print("\n--------------------------------------------------")
        print("INCORRECT PIN. PLEASE TRY AGAIN.")
        print("--------------------------------------------------")
        pin = input("RE-ENTER YOUR PIN: ")
        attempts += 1
        if attempts == 2:
            print("\n==================================================")
            print("ACCOUNT LOCKED DUE TO MULTIPLE INCORRECT ATTEMPTS.")
            print("PLEASE CONTACT YOUR BANK BRANCH.")
            print("==================================================")
            quit()

# -----------------------------------------------
# Post-login message
# -----------------------------------------------
if attempts < 3:
    print("\n==================================================")
    print("                LOGIN SUCCESSFUL                  ")
    print("==================================================")
    print("PLEASE CHOOSE FROM THE FOLLOWING OPTIONS:")
    print("--------------------------------------------------")

# -----------------------------------------------
# Main ATM Menu Loop
# -----------------------------------------------
# this prints a main menu
while True:
    print("\n================ MAIN MENU =================")
    print("1. CHECK BALANCE")
    print("2. WITHDRAW CASH")
    print("3. DEPOSIT CASH")
    print("4. CHANGE PIN")
    print("5. MINI STATEMENT")
    print("6. EXIT")
    print("============================================")

    choice = input("ENTER YOUR CHOICE (1-6): ")

    # -------------------------------
    # Option 1: Check balance
    # -------------------------------
    if choice == '1':
        print("\n==================================================")
        print(f"YOUR CURRENT BALANCE IS ₹{account['balance']}")
        print("==================================================")
        receipt = input("WOULD YOU LIKE A PRINTED BALANCE RECEIPT? (yes/no): ").lower()
        if receipt == 'yes':
            print("\n================ BALANCE RECEIPT =================")
            print(f"ACCOUNT HOLDER   : {account['name']}")
            print(f"AVAILABLE BALANCE: ₹{account['balance']}")
            print(f"TRANSACTIONS THIS SESSION: {len(account['transactions'])}")
            print("==================================================")
            print("PLEASE TAKE YOUR RECEIPT.")
            break
        else:
            print("\nTHANK YOU FOR USING DK BANK ATM.")
            break

    # -------------------------------
    # Option 2: Withdraw cash
    # -------------------------------
    elif choice == '2':
        withdrawamount = input("ENTER AMOUNT TO WITHDRAW (IN ₹): ")

        if not withdrawamount.isdigit():
            print("\nPLEASE ENTER A VALID NUMBER.")
            continue
        else:
            amount = int(withdrawamount)
            if amount <= 0:
                print("\nAMOUNT MUST BE GREATER THAN ZERO.")
            elif amount > account['balance']:
                print("\nINSUFFICIENT BALANCE.")
            else:
                account['balance'] -= amount
                account['transactions'].append({"type": "Withdrawal", "amount": amount})
                print("\nPROCESSING YOUR REQUEST... PLEASE WAIT...")
                print("--------------------------------------------------")
                print("TRANSACTION SUCCESSFUL. PLEASE COLLECT YOUR CASH.")
                print("--------------------------------------------------")
                remaining = amount
                notes = [2000, 500, 200, 100]
                print("\nNOTES DISPENSED:")
                for note in notes:
                    count = remaining // note
                    if count > 0:
                        print(f"₹{note} x {count}")
                        remaining -= note * count
                print("--------------------------------------------------")
                check_balance = input("WOULD YOU LIKE TO CHECK YOUR BALANCE? (yes/no): ").lower()
                if check_balance == 'yes':
                    print(f"\nYOUR CURRENT BALANCE IS ₹{account['balance']}")
                receipt = input("WOULD YOU LIKE A RECEIPT FOR THIS TRANSACTION? (yes/no): ").lower()
                if receipt == 'yes':
                    print("\n================ TRANSACTION RECEIPT ================")
                    print("TRANSACTION TYPE   : WITHDRAWAL")
                    print(f"AMOUNT WITHDRAWN   : ₹{amount}")
                    print(f"REMAINING BALANCE  : ₹{account['balance']}")
                    print("=====================================================")
                    print("PLEASE TAKE YOUR CASH AND RECEIPT.")
                    break
                else:
                    print("\nTHANK YOU FOR USING DK BANK ATM.")
                    break

    # -------------------------------
    # Option 3: Deposit cash
    # -------------------------------
    elif choice == '3':
        depositamount = input("ENTER AMOUNT TO DEPOSIT (IN ₹): ")

        if not depositamount.isdigit():
            print("\nPLEASE ENTER A VALID NUMBER.")
        else:
            amount = int(depositamount)
            if amount <= 0:
                print("\nAMOUNT MUST BE GREATER THAN ZERO.")
            else:
                account['balance'] += amount
                account['transactions'].append({"type": "Deposit", "amount": amount})
                print("\nPLEASE WAIT WHILE WE PROCESS YOUR DEPOSIT...")
                print("--------------------------------------------------")
                print("DEPOSIT SUCCESSFUL.")
                print("--------------------------------------------------")
                check_balance = input("WOULD YOU LIKE TO CHECK YOUR BALANCE? (yes/no): ").lower()
                if check_balance == 'yes':
                    print(f"\nYOUR CURRENT BALANCE IS ₹{account['balance']}")
                receipt = input("WOULD YOU LIKE A RECEIPT FOR THIS TRANSACTION? (yes/no): ").lower()
                if receipt == 'yes':
                    print("\n================ TRANSACTION RECEIPT ================")
                    print("TRANSACTION TYPE   : DEPOSIT")
                    print(f"AMOUNT DEPOSITED   : ₹{amount}")
                    print(f"NEW BALANCE        : ₹{account['balance']}")
                    print("=====================================================")
                    print("PLEASE TAKE YOUR RECEIPT.")
                    break
                else:
                    print("\nTHANK YOU FOR USING DK BANK ATM.")
                    break

    # -------------------------------
    # Option 4: Change PIN
    # -------------------------------
    elif choice == '4':
        print("\n==================================================")
        print("                 CHANGE PIN MENU                  ")
        print("==================================================")
        currentPin = input("ENTER YOUR CURRENT PIN: ")
        if currentPin != pin:
            print("\nINCORRECT CURRENT PIN. PIN NOT CHANGED.")
        else:
            newpin1 = input("ENTER NEW 4-DIGIT PIN: ")
            newpin2 = input("CONFIRM NEW PIN: ")
            if not newpin1.isdigit():
                print("\nPIN MUST CONTAIN DIGITS ONLY.")
                break
            elif len(newpin1) != 4:
                print("\nPIN MUST BE 4 DIGITS LONG.")
                break
            elif newpin1 != newpin2:
                print("\nPINs DO NOT MATCH.")
                break
            else:
                accounts[newpin1] = accounts.pop(pin)
                pin = newpin1
                print("\nPIN UPDATED SUCCESSFULLY.")
                print("PLEASE REMEMBER YOUR NEW PIN.")
                print("==================================================")
                break

    # -------------------------------
    # Option 5: Mini Statement
    # -------------------------------
    elif choice == '5':
        print("\n================ MINI STATEMENT ==================")
        print(f"ACCOUNT HOLDER   : {account['name']}")
        print(f"AVAILABLE BALANCE: ₹{account['balance']}")
        print("--------------------------------------------------")
        if not account['transactions']:
            print("NO TRANSACTIONS FOUND.")
        else:
            print("LAST 5 TRANSACTIONS:")
            for t in account['transactions'][-5:]:
                print(f"{t['type']:<15} ₹{t['amount']}")
        print("==================================================")
        print("THANK YOU FOR USING DK BANK ATM.")
        break

    # -------------------------------
    # Option 6: Exit ATM
    # -------------------------------
    elif choice == '6':
        print("\n==================================================")
        print("         THANK YOU FOR USING DK BANK ATM          ")
        print("==================================================")
        print("PLEASE COLLECT YOUR CARD AND RECEIPT.")
        print("--------------------------------------------------")
        break

    else:
        print("\nINVALID CHOICE. PLEASE ENTER A NUMBER BETWEEN 1 AND 6.")
