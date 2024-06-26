class Account:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}"
        return "Insufficient funds or invalid withdrawal amount"

    def display_balance(self):
        return f"Account {self.account_number} balance: ${self.balance:.2f}"

class SavingsAccount:
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}"
        return "Insufficient funds or invalid withdrawal amount"

    def display_balance(self):
        return f"Savings Account {self.account_number} balance: ${self.balance:.2f}"

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return f"Added ${interest:.2f} interest"

class CheckingAccount:
    def __init__(self, account_number, balance, overdraft_limit):
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}"
        return "Insufficient funds or invalid withdrawal amount"

    def display_balance(self):
        return f"Checking Account {self.account_number} balance: ${self.balance:.2f}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        return f"Added account {account.account_number}"

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return f"Removed account {account.account_number}"
        return "Account not found"

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)
        return f"Opened account {account.account_number}"

    def close_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return f"Closed account {account.account_number}"
        return "Account not found"

# Example usage
if __name__ == "__main__":
    # Create a bank
    bank = Bank("MyBank")

    # Create a customer
    customer = Customer("John Doe")

    # Open a regular account
    account = Account("A001", 1000, "Regular")
    customer.open_account(account)
    bank.add_account(account)

    # Open a savings account
    savings = SavingsAccount("SA001", 1000, 2.5)
    customer.open_account(savings)
    bank.add_account(savings)

    # Open a checking account
    checking = CheckingAccount("CA001", 500, 100)
    customer.open_account(checking)
    bank.add_account(checking)

    # Perform some transactions
    print(account.deposit(500))
    print(account.display_balance())

    print(savings.deposit(500))
    print(savings.display_balance())
    print(savings.add_interest())
    print(savings.display_balance())

    print(checking.withdraw(600))
    print(checking.display_balance())

    # Close an account
    print(customer.close_account(checking))
    print(bank.remove_account(checking))

    # Try to find accounts
    found_account = bank.find_account("SA001")
    if found_account:
        print(f"Found account: {found_account.display_balance()}")
    else:
        print("Account not found")

    not_found_account = bank.find_account("CA001")
    if not_found_account:
        print(f"Found account: {not_found_account.display_balance()}")
    else:
        print("Account not found")