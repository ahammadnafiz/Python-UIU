from datetime import datetime

class Account:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def transfer(self, amount, destination_account):
        if self.balance >= amount:
            self.balance -= amount
            destination_account.balance += amount
        else:
            print("Insufficient balance.")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance, account_holder, overdraft_limit):
        super().__init__(account_number, balance, account_holder)
        self.overdraft_limit = overdraft_limit

class CreditCardAccount(Account):
    def __init__(self, account_number, balance, account_holder, credit_limit):
        super().__init__(account_number, balance, account_holder)
        self.credit_limit = credit_limit

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def display_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: {account.balance}")

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now()

    def process_transaction(self, account):
        if self.transaction_type == 'deposit':
            account.deposit(self.amount)
        elif self.transaction_type == 'withdraw':
            account.withdraw(self.amount)
        elif self.transaction_type == 'transfer':
            destination_account = self.prompt_for_destination_account()
            account.transfer(self.amount, destination_account)

    def reverse_transaction(self, account):
        if self.transaction_type == 'deposit':
            account.withdraw(self.amount)
        elif self.transaction_type == 'withdraw':
            account.deposit(self.amount)
        elif self.transaction_type == 'transfer':
            destination_account = self.prompt_for_destination_account()
            destination_account.transfer(self.amount, account)

    def display_transaction_details(self):
        print(f"Transaction Type: {self.transaction_type}, Amount: {self.amount}, Date: {self.date}")

    def prompt_for_destination_account(self):
        # Assuming user provides the destination account number
        destination_account_number = input("Enter the destination account number: ")
        destination_account = None

        # Find the destination account in the bank's customers' accounts
        for customer in bank.customers:
            for account in customer.accounts:
                if account.account_number == destination_account_number:
                    destination_account = account
                    break

        if destination_account is None:
            print("Destination account not found.")

        return destination_account

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.transactions = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def process_transaction(self, transaction):
        self.transactions.append(transaction)
        transaction.process_transaction()

    def generate_reports(self):
        print(f"Bank Name: {self.name}")
        print("Financial Report:")
        print("===================================")

        total_balance = 0
        for customer in self.customers:
            print(f"Customer Name: {customer.name}")

            for account in customer.accounts:
                print(f"Account Number: {account.account_number}")
                print(f"Balance: {account.balance}")
                print("-------------------")

                total_balance += account.balance

            print("===================")

        print(f"Total Bank Balance: {total_balance}")
        print("===================================")

# Test Cases
bank = Bank('Nafiz')
# Create bank accounts
savings_account = SavingsAccount("SA001", 10000, "John Doe", 0.05)
checking_account = CheckingAccount("CA001", 5000, "John Doe", 1000)
credit_card_account = CreditCardAccount("CC001", 0, "John Doe", 5000)

# Create customer and add accounts
customer = Customer("John Doe", "123 Main Street")
customer.add_account(savings_account)
customer.add_account(checking_account)
customer.add_account(credit_card_account)

# Display customer accounts
customer.display_accounts()

# Perform transactions
transaction1 = Transaction("deposit", 2000)
transaction1.process_transaction(savings_account)

transaction2 = Transaction("withdraw", 1000)
transaction2.process_transaction(checking_account)

transaction3 = Transaction("transfer", 500)
transaction3.process_transaction(checking_account)

# Display customer accounts after transactions
customer.display_accounts()

# Reverse a transaction
transaction2.reverse_transaction(checking_account)

# Display customer accounts after reversing a transaction
customer.display_accounts()