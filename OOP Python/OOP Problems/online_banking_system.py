class Account:
    def __init__(self, account_number, initial_balance) -> None:
        self._account_number = account_number
        self._balance = initial_balance
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Amount must be positive')
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds.")
                
    
class SavingsAccount(Account):
    def __init__(self, account_number, initial_balance, interest_rate) -> None:
        super().__init__(account_number, initial_balance)
        self._interest_rate = interest_rate
        self.withdraw_count = 0
    def calculate_interest(self):
        interest = self._balance * (self._interest_rate / 100) 
        self.deposit(interest + self._balance)
        print(interest)
    
    def withdraw(self, amount):
        fee = 10
        
        if self.withdraw_count < 3:
            if self._balance - amount >= 1000:
                self._balance += amount
                print(f"Withdrew ${amount}. New balance: ${self._balance}")
                self.withdraw_count += 1
            else:
                print("Withdrawal failed. Minimum balance requirement not met.")
        else:
            if self._balance - (amount + fee) > 1000:
                self._balance += (amount + fee)
                print(f"Withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("Withdrawal failed. Minimum balance requirement not met.")
        

class FixedAccount(Account):
    def __init__(self, account_number, initial_balance, limit) -> None:
        super().__init__(account_number, initial_balance)
        self._limit = limit
    
    def withdraw(self, amount):
        if amount <= self._limit:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded.")

class CheckingAccount(Account):
    def __init__(self, account_number, initial_balance, overdraft_limit) -> None:
        super().__init__(account_number, initial_balance)
        self._overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= self._balance + self._overdraft_limit:
            super().withdraw(amount)
        else:
            print("Exceeded overdraft limit.")

class BusinessAccount(Account):
    def __init__(self, account_number, initial_balance,  transaction_fee) -> None:
        super().__init__(account_number, initial_balance)
        self._transaction_fee =  transaction_fee
    
    def withdraw(self, amount):
        fee = amount * (self._transaction_fee / 100)
        super().withdraw(amount + fee)
        print(f"Transaction fee of ${fee} deducted. New balance: ${self._balance}")


# Example: Deposit and Withdraw
account1 = Account(1001, 1000)
account1.deposit(500)
account1.withdraw(200)

# Example: Calculate Interest
savings_account = SavingsAccount(2001, 5000, 2)
savings_account.calculate_interest()

# Example: Enforce Withdrawal Limit
fixed_account = FixedAccount(3001, 3000, 1000)
fixed_account.withdraw(800)

# Example: Overdraft Limit
checking_account = CheckingAccount(4001, 2000, 500)
checking_account.withdraw(2500)

# Example: Transaction Fee
business_account = BusinessAccount(5001, 10000, 1.5)
business_account.withdraw(500)