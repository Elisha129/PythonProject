import random

def menu():
    """
    Display the main menu and get user's choice.

    Returns:
        str: User choice (1-8).
    """
    print("\nPlease select an option (1 to 8):")
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Close account")
    print("6. Display all account holders")
    print("7. Total balance in the bank")
    print("8. Quit")
    return input("Enter your choice: ").strip()

def create_account(accounts):
    """
    Create a new bank account and add it to accounts.

    Args:
        accounts (dict): Dictionary containing all bank accounts.
    """
    first_name = input("Enter first name: ").strip().capitalize()
    while not first_name.isalpha():
        first_name = input("First name must contain only letters. Try again: ").strip().capitalize()

    last_name = input("Enter last name: ").strip().capitalize()
    while not last_name.isalpha():
        last_name = input("Last name must contain only letters. Try again: ").strip().capitalize()

    id_number = input("Enter ID number: ").strip()
    while len(id_number) != 9 or not id_number.isdigit() or id_number in accounts:
        if not id_number.isdigit() or len(id_number) != 9:
            id_number = input("ID must be 9 digits. Try again: ").strip()
        else:
            id_number = input("ID already exists. Enter a new ID: ").strip()

    birth_date = input("Enter birth date (DD/MM/YYYY): ").strip()
    while not validate_birth_date(birth_date):
        birth_date = input("Invalid format or age. Enter birth date (DD/MM/YYYY): ").strip()

    email = input("Enter email address: ").strip()
    while not ("@" in email and email.endswith(".com")):
        email = input("Invalid email. Try again: ").strip()

    account_number = generate_unique_account_number(accounts)

    accounts[id_number] = {
        'first_name': first_name,
        'last_name': last_name,
        'birth_date': birth_date,
        'email': email,
        'account_number': account_number,
        'balance': 0.0,
        'id_number': id_number
    }

    print("\nAccount created successfully!")
    print(f"Account number: {account_number}\nName: {first_name} {last_name}\nID: {id_number}\nBirth date: {birth_date}\nEmail: {email}")

def generate_unique_account_number(accounts):
    """Generate a unique 4-digit account number."""
    while True:
        number = random.randint(1000, 9999)
        if number not in [acc['account_number'] for acc in accounts.values()]:
            return number

def validate_birth_date(birth_date):
    """Validate birth date format and minimum age."""
    if len(birth_date) != 10 or birth_date[2] != '/' or birth_date[5] != '/':
        return False
    try:
        day, month, year = map(int, birth_date.split('/'))
        if year < 1900 or year > 2024 or (2024 - year) < 16:
            return False
    except ValueError:
        return False
    return True

def deposit_money(accounts):
    """Deposit money into an account."""
    account_number = input("Enter account number: ").strip()
    account = find_account_by_number(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: ").strip())
        if amount <= 0:
            raise ValueError
        account['balance'] += amount
        print(f"Deposit successful. Updated balance: {account['balance']}")
    except ValueError:
        print("Invalid amount. Deposit cancelled.")

def withdraw_money(accounts):
    """Withdraw money from an account with authentication."""
    account_number = input("Enter account number: ").strip()
    account = find_account_by_number(accounts, account_number)

    if not account:
        print("Account not found.")
        return

    id_number = input("Enter your ID number: ").strip()
    birth_date = input("Enter your birth date (DD/MM/YYYY): ").strip()

    if not authenticate_user(account, id_number, birth_date):
        print("Authentication failed.")
        return

    try:
        amount = float(input("Enter withdrawal amount: ").strip())
        if amount <= 0 or account['balance'] - amount < -1000:
            print("Invalid amount or insufficient funds.")
            return
        account['balance'] -= amount
        print(f"Withdrawal successful. Updated balance: {account['balance']}")
    except ValueError:
        print("Invalid amount entered.")

def check_balance(accounts):
    """Check balance for an account."""
    account_number = input("Enter account number: ").strip()
    account = find_account_by_number(accounts, account_number)
    if account:
        print(f"Balance: {account['balance']}")
    else:
        print("Account not found.")

def close_account(accounts):
    """Close an account after authentication."""
    account_number = input("Enter account number: ").strip()
    account = find_account_by_number(accounts, account_number)
    if not account:
        print("Account not found.")
        return

    id_number = input("Enter your ID number: ").strip()
    birth_date = input("Enter your birth date (DD/MM/YYYY): ").strip()

    if authenticate_user(account, id_number, birth_date):
        del accounts[account['id_number']]
        print("Account closed successfully.")
    else:
        print("Authentication failed.")

def display_all_accounts(accounts):
    """Display all accounts in the bank."""
    if not accounts:
        print("No accounts in the bank.")
    else:
        for acc in accounts.values():
            print(f"\nName: {acc['first_name']} {acc['last_name']}")
            print(f"Account Number: {acc['account_number']}\nID: {acc['id_number']}\nEmail: {acc['email']}")

def total_bank_balance(accounts):
    """Display total balance across all accounts."""
    total = sum(acc['balance'] for acc in accounts.values())
    print(f"Total bank balance: {total}")

def find_account_by_number(accounts, account_number):
    """Find account object by account number."""
    for acc in accounts.values():
        if str(acc['account_number']) == account_number:
            return acc
    return None

def authenticate_user(account, id_number, birth_date):
    """Check if the user credentials match the account."""
    return account['id_number'] == id_number and account['birth_date'] == birth_date

def main():
    accounts = {}
    while True:
        choice = menu()
        match choice:
            case '1':
                create_account(accounts)
            case '2':
                deposit_money(accounts)
            case '3':
                withdraw_money(accounts)
            case '4':
                check_balance(accounts)
            case '5':
                close_account(accounts)
            case '6':
                display_all_accounts(accounts)
            case '7':
                total_bank_balance(accounts)
            case '8':
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == '__main__':
    main()
