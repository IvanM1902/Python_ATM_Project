# Python Simple ATM Console Application
This repository contains a basic ATM (Automated Teller Machine) console application designed to simulate fundamental banking operations. The project's core challenge and learning experience revolved around managing data persistence using CSV files, including handling user registration, account creation, and money transfers.

## 💡 Project Overview
This console application provides a simplified banking system where users can register, log in, create multiple bank accounts, and transfer funds between accounts within the bank. All user and account data, including transaction history, is persistently stored and managed using CSV (Comma Separated Values) files, mimicking a rudimentary database system. The project particularly emphasizes robust handling of CSV data for reads, writes, and deletions.

## ✨ Features
User Registration & Login: Allows new users to register and existing users to securely log into their bank accounts.

Account Management: Users can create multiple bank accounts under their profile.

Fund Transfers: Enables users to transfer money between different bank accounts within the system.

CSV-based Data Storage: All user, account, and transaction data is stored in and retrieved from CSV files.

Data Persistence: Information remains available even after the application is closed and reopened.

## 🛠️ Technologies Used
Programming Language: Python

Data Storage: CSV (Comma Separated Values) files

Core Concepts: File I/O, data parsing, basic security (for login), and data manipulation.

## 🚀 Getting Started
To run this application:

Clone the repository:

git clone https://github.com/IvanM1902/Python_ATM_Project.git
cd Python_ATM_Project

Run the application:

python main.py

The application will typically create the necessary CSV files (customers.csv, accounts.csv, accountsTransactions.csv) if they don't already exist when you run it for the first time.

## 📂 Project Structure
.
├── main.py                     # Main application logic for the ATM system
├── customers.csv               # Stores user registration data (ID, username, password, age)
├── accounts.csv                # Stores bank account details (username, account number, type, IBAN, funds)
├── accountsTransactions.csv    # Records all transactions (ID, account number, type, amount, date)
└── README.md

## 🧠 Learning & Challenges
The most challenging aspects of this project involved:

Correct CSV Data Handling: Ensuring data was correctly read, parsed, written, and updated in the CSV files. This included handling various data types and maintaining the integrity of records.

Deleting Data: Implementing reliable methods to remove specific records from CSV files without corrupting the entire dataset, which required careful file rewriting.

Data Integrity: Maintaining consistency across multiple CSV files (e.g., ensuring account balances are updated correctly after transfers, and transaction logs accurately reflect operations). Implementing checks for existing usernames, account numbers, and transfer IBANs was crucial.

This project provided valuable hands-on experience with fundamental data management principles and file I/O operations in Python, demonstrating robust problem-solving skills in a practical context.

## 🤝 Contributing
This project was developed as a personal learning exercise. While not actively seeking external contributions for this specific academic version, feel free to fork the repository, experiment, and adapt it for your own purposes.
