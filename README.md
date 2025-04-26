🏦 Banking System Project (Python)

A simple console-based banking system for creating and managing bank accounts.  
Built with a focus on input validation, error handling, and clean design.

----------------------------------------------------------------------------------------------------------------
📚 Problem Statement
Managing basic banking operations like account creation, deposits, withdrawals, and balance checking often involves repetitive tasks prone to input errors.
-----------------------------------------------------------------------------------------------------------------
🎯 Solution
This project provides a simple and safe banking system that allows users to:
- Create a bank account.
- Deposit and withdraw money with validation.
- Check account balances securely.
- Close accounts with authentication.
- View all account holders.
- Check the total balance of the bank.
-----------------------------------------------------------------------------------------------------------------
 👤 Target Audience
- Beginner programmers looking for an introduction to real-world projects.
- Anyone interested in seeing input validation, error handling, and user authentication in a Python project.
-----------------------------------------------------------------------------------------------------------------
 🚀 MVP Features (Version 1.0)
- [x] User authentication using ID number and birthdate.
- [x] Create a new bank account.
- [x] Deposit and withdraw funds with safeguards.
- [x] Check the balance of an account.
- [x] Display a list of all account holders.
- [x] Display total bank balance.

-----------------------------------------------------------------------------------------------------------------
📈 Planned Features (Future Versions)
- [ ] Save accounts to a file and load on startup.
- [ ] Password protection for accounts.
- [ ] GUI interface using Tkinter.
- [ ] Advanced reports: Top 5 richest customers.
-----------------------------------------------------------------------------------------------------------------
⚙️ Technology Stack
- Python 3.10+
 Project Structure
-----------------------------------------------------------------------------------------------------------------
📋 Project Structure
 🧠 Key Concepts Used
- Functions and modular design
- Input validation and error handling (try/except)
- Enum-like handling with `match-case` (Python 3.10 feature)
- Basic authentication logic
- Dictionary data structures for storing accounts
- Loops and conditionals for menu navigation
-----------------------------------------------------------------------------------------------------------------
 📢 Notes
- All account numbers are 4-digit random numbers (1000–9999).
- Withdrawal is allowed up to a limit of `-1000` overdraft.
- Users must be at least 16 years old to open an account.
