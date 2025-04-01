def menu():
    """""
    This function is the function of the main manu.

    Prints: the main manu.

    returns: the user choice (1-8) as a string.
    """

    print("Please enter one of the options (1 to 8):")
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check Balance in account")
    print("5. Close account")
    print("6. Display all accounts holder list")
    print("7. Total Balance in the Bank")
    print("8. Quit")
    choice = input("Enter your choice: ")
    return choice


def create_account(accounts):
    """""
    This function allows the user to create their own bank account
    by providing their first name, last name,
    ID number, email, and birthdate.
    It validates each input to ensure correctness and generates a unique
    account number for the new account.

    Args:

        "accounts" : a dictionary contain all the bank accounts and thire details.

    Example:
       " >>> accounts = {}
        >>> create_account(accounts)
        Enter first name: Shimon
        Enter last name: David
        Enter ID number: 123456789
        Enter birthdate (YYYY/MM/DD): 1990/01/01
        Enter email address: shimon.david@gmail.com

        Account created successfully.
        New account details:
        Account number: 1234
        Name: John Doe
        ID number: 123456789
        Birth date: 1990/01/01
        Email: john.doe@example.com

    """

    # Get customer details from user
    first_name = input("Enter first name: ").capitalize()
    while not first_name.isalpha():
        print("First name must contain only letters.")
        first_name = input("Enter first name: ").capitalize()

    last_name = input("Enter last name: ").capitalize()
    while not last_name.isalpha():
        print("Last name must contain only letters.")
        last_name = input("Enter last name: ").capitalize()

    id_number = input("Enter ID number: ")
    while len(id_number) != 9 or not id_number.isdigit() or id_number in accounts:
        if not id_number.isdigit() or len(id_number) != 9:
            print("ID number must contain 9 digits.")
            id_number = input("Enter ID number: ")
        elif id_number in accounts:
            print("ID number is already registered")
            id_number = input("Enter ID number: ")

    birth_date = input("Enter birth date (DD/MM/YYYY): ")
    while not birth_date or len(birth_date) != 10 or birth_date[2] != '/' or birth_date[5] != '/':
        print("Invalid birth date format. Please use DD/MM/YYYY.")
        birth_date = input("Enter birth date (DD/MM/YYYY): ")

    birth_year = int(birth_date[6:])
    while birth_year <= 1900:
        print("Invalid birth year. Year must be greater than 1900.")
        birth_date = input("Enter birth date (DD/MM/YYYY): ")
        birth_year = int(birth_date[6:])

    current_year = 2024  # Assuming the current year is 2024
    age = current_year - birth_year
    while age < 16:
        print("Cannot open a bank account for individuals under 16 years old.")
        birth_date = input("Enter birth date (DD/MM/YYYY): ")
        birth_year = int(birth_date[6:])
        current_year = 2024
        age = current_year - birth_year

    email = input("Enter email address: ")
    while '@' not in email or email.count('@') != 1 or not email.endswith('.com'):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter email address: ")

    # Generate a new account number
    import random
    account_number = random.randint(1000, 9999)
    while account_number in accounts.values():
        account_number = random.randint(1000, 9999)

    # Add the new account to the accounts dictionary
    accounts[id_number] = {
        'first_name': first_name.capitalize(),
        'last_name': last_name.capitalize(),
        'birth_date': birth_date,
        'email': email,
        'account_number': account_number,
        'balance': 0.0,
        'id_number': id_number  # Adding ID number to the account details
    }

    print("Account created successfully.")
    print("New account details:")
    print("Account number:", account_number)
    print("Name:", first_name.capitalize(), last_name.capitalize())
    print("ID number:", id_number)
    print("Birth date:", birth_date)
    print("Email:", email)


def deposit_money(accounts):
    """""
    Deposit money into a chosen account.

    This function allows the user to deposit money into a specified account.
    It prompts the user to enter the account number and the deposit amount.
    If the account exists, the deposit is made and the balance
    is updated accordingly.

    Args:

        "accounts" : a dictionary contain all the bank accounts

    Example:
        accounts = {'123456789'}(=id) : {'first_name': 'Shimon', 'last_name': 'David',
        'birth_date': '1990/01/01','email' :
        'Shimon.david@gmail.com', 'account_number': 1234, 'balance': 1000.0}
        >>> deposit_money(accounts)
        Enter account number: 1234
        Enter deposit amount: 500

        Deposit successful.
        Account number: 1234
        Updated balance: 1500.0

    """
    # Get account number from user
    account_number = input("Enter account number: ")

    # Check if account exists
    if account_number not in [str(account['account_number']) for account in accounts.values()]:
        print("Account not found.")
        return

    # Get deposit amount from user
    while True:
        try:
            deposit_amount = float(input("Enter deposit amount: "))
            break  # If conversion to float succeeds, exit the loop
        except ValueError:
            print("Invalid input. Please enter a valid number without strings.")

    # Find the account and update balance
    for account in accounts.values():
        if str(account['account_number']) == account_number:
            account['balance'] += deposit_amount
            print("Deposit successful.")
            print("Account number:", account_number)
            print("Updated balance:", account['balance'])
            return

    print("Deposit failed.")


def withdraw_money(accounts):
    """
    Withdraw money from a chosen account.

    This function allows the user to withdraw money from a specified account.
    It prompts the user to enter the account number and the withdrawal a chosen amount.
    If the account exists and the account balance is within the limits (between -1000 and 1000),
    the withdrawal is made and the balance is updated accordingly.

    Args:

        "accounts": a dictionary contain all the bank accounts

    Example:

        accounts = {'123456789'(=id): {'first_name': 'Simon', 'last_name': 'David', 'birth_date': '1990/01/01',
        ... 'email': 'Shimon.David@gmail.com', 'account_number': 1234, 'balance': 1000.0}}
        withdraw_money(accounts)
        Enter account number: 1234
        Enter withdrawal amount: 500
        Withdrawal successful.
        Account number: 1234
        Updated balance: 500.0

    """

    # Get account number from user
    account_number = input("Enter account number: ")

    # Get user's ID number and birthdate for authentication
    id_number = input("Enter your ID number: ")
    birth_date = input("Enter your birth date (DD/MM/YYYY): ")

    # Authenticate user
    if not user_authenticate(accounts, account_number, id_number, birth_date):
        print("Authentication failed. Unable to withdraw money.")
        return

    # Check if account exists
    if account_number not in [str(account['account_number']) for account in accounts.values()]:
        print("Account not found.")
        return

    # Find the account
    account = None
    for acc in accounts.values():
        if str(acc['account_number']) == account_number:
            account = acc
            break

    # Get withdrawal amount from user
    while True:
        withdrawal_amount = input("Enter withdrawal amount: ")
        if not withdrawal_amount.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        withdrawal_amount = float(withdrawal_amount)
        if withdrawal_amount <= 0:
            print("Withdrawal amount must be positive.")
        elif account['balance'] - withdrawal_amount < -1000:
            print("Insufficient funds. You can withdraw up to", account['balance'] + 1000)
        else:
            break

    # Update account balance
    account['balance'] -= withdrawal_amount
    print("Withdrawal successful.")
    print("Account number:", account_number)
    print("Updated balance:", account['balance'])


def check_balance(accounts, account_number):
    """
    Check the balance of a chosen account.

    This function allows the user to check the balance of a specified account.
    It prompts the user to enter the account number. If the account exists,
    it prints the current balance of the account.

    Args:

        accounts : a dictionary contain all the bank accounts.
        account_number : the number of the chosen account.

    Example:

        accounts = {'123456789'(=id): {'first_name': 'Simon', 'last_name': 'David', 'birth_date': '1990/01/01',
        ... 'email': 'Shimon.david@gmail.com', 'account_number': 1234, 'balance': 1000.0}}
        check_balance(accounts, '1234')
        Account balance for account 1234: 1000.0

    """

    # Check if the account number exists in the accounts dictionary
    if int(account_number) in [account['account_number'] for account in accounts.values()]:
        # Get user's balance from the accounts dictionary
        balance = next(
            account['balance'] for account in accounts.values() if account['account_number'] == int(account_number))
        # Print the balance
        print(f"Account balance for account {account_number}: {balance}")
    else:
        print("Account number not found.")


def close_account(accounts, account_number):
    """
    Close a chosen account.

    This function allows the user to close a specified account.
    It prompts the user to enter the account number. If the account exists,
    it deletes the account from the accounts' dictionary.

    Args:

        accounts: a dictionary contain all the bank accounts
        account_number: the number of the chosen account

    Example:
        accounts = {'123456789'(=id): {'first_name': 'Simon', 'last_name': 'David', 'birth_date': '1990/01/01',
        ... 'email': 'shimon.david@gmail.com', 'account_number': 1234, 'balance': 1000.0}}
        close_account(accounts, '1234')
        Account 1234 has been closed successfully.

    """
    # Check if the account number exists in the accounts dictionary
    account_to_close = None
    for acc_id, account in accounts.items():
        if account['account_number'] == int(account_number):
            account_to_close = acc_id
            break

    # Authenticate user
    if not account_to_close:
        print("Account not found.")
        return

    id_number = input("Enter your ID number: ")
    birth_date = input("Enter your birth date (DD/MM/YYYY): ")
    if not user_authenticate(accounts, str(account_number), id_number, birth_date):
        print("Authentication failed. Unable to close account.")
        return

    # Delete the account from the accounts dictionary
    del accounts[account_to_close]
    print(f"Account {account_number} has been closed successfully.")


def display_all_accounts(accounts):
    """
        Display all existing accounts.

        This function displays information about all existing accounts. If there are no accounts,
        it prints a message indicating that there are no accounts in the bank.

        Args:

            accounts: a dictionary contain all the bank accounts.

        Example:
            accounts = {'123456789'(=id): {'first_name': 'Simon', 'last_name': 'David', 'birth_date': '1990/01/01',
            ...'email': 'shimon.david@david.com', 'account_number': 1234, 'balance': 1000.0}}
            display_all_accounts(accounts)
            List of all account holders:
            Account holder: John Doe
            Account number: 1234
            ID number: 123456789
            Email: Shimon.david@gmail.com
    """
    if not accounts:
        print("There are no accounts in the bank.")
    else:
        print("List of all account holders:")
        for id_number, account_info in accounts.items():
            print(f"Account holder: {account_info['first_name']} {account_info['last_name']}")
            print(f"Account number: {account_info['account_number']}")
            print(f"ID number: {id_number}")
            print(f"Email: {account_info['email']}")
            print()


def user_authenticate(accounts, account_number, id_number, birth_date):
    """
    Authenticate user credentials.

    This function checks if the provided account number exists in the accounts' dictionary. If it does, it compares
    the provided ID number and birthdate with the stored information to authenticate the user.

    Args:
        accounts: a dictionary contain all the bank number
        account_number: the number of the chosen account
        id_number: the id number the belongs to the chosen account
        birth_date: the birthdate of the owner of the chosen account

    Returns:
        bool: True if authentication is successful, False otherwise.


    Example:
        accounts = {'123456789': {'first_name': 'Simon', 'last_name': 'David', 'birth_date': '1990/01/01',
        ...'email': 'shimon.david@gmail.com', 'account_number': 1234, 'balance': 1000.0}}
        user_authenticate(accounts, '1234', '123456789', '1990/01/01')
        True

    """
    # Check if the account number exists in the accounts dictionary
    if account_number not in [str(account['account_number']) for account in accounts.values()]:
        print("Account not found.")
        return False

    # Get the account details
    account_details = next(account for account in accounts.values() if str(account['account_number']) == account_number)

    # Check if the provided account details match with the stored ones
    if (account_details['id_number'] == id_number and
            account_details['birth_date'] == birth_date):
        return True
    else:
        print("Authentication failed. Please check your details and try again.")
        return False


def total_bank_balance(accounts):
    """
    Calculate the total balance in the bank.

    This function calculates the total balance by summing up the balances
    of all the accounts in the bank.

    Args:
        accounts: A dictionary containing all the bank accounts.

    Returns:
        float: The total balance in the bank.

    """
    total_balance = sum(account['balance'] for account in accounts.values())
    print("Total Balance in the Bank:", total_balance)


def main():
    """
    The main function of the banking system.

    This function serves as the entry point for the banking system.
    It continuously prompts the user to select options from the menu until the user chooses
    to quit the system (option 8). Each option corresponds to a specific
    operation such as creating a new account, depositing money, withdrawing money,
    checking balance, closing an account,
    displaying all account holders, and checking the total balance in the bank.

    Args: none



    """

    accounts = {}
    while True:
        # Get users choice from the menu
        choice = menu()

        # Use match case to handle users choice
        match choice:
            case '1':
                # Create a new account
                create_account(accounts)
            case '2':
                # Deposit money into an account
                deposit_money(accounts)
            case '3':
                # Withdraw money from an account
                withdraw_money(accounts)
            case '4':
                # Check the balance of an account
                account_number = int(input("Enter account number: "))
                check_balance(accounts, account_number)

            case '5':
                # Close an account
                account_number = int(input("Enter account number: "))
                close_account(accounts, account_number)

            case '6':
                # Display all account holders
                display_all_accounts(accounts)
            case '7':
                # Check the total balance in the bank
                total_bank_balance(accounts)
            case '8':
                # Exit the system
                print("Exiting the system")
                break
            case _:
                # Handle invalid choice
                print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == '__main__':
    main()
