class Bank:
    def __init__(self, account_type, initial_balance) -> None:
        if account_type == 'Savings':
            if initial_balance < 1000:
                raise ValueError('Initial Balance Must be 1000 for savings account')
            self.account_type = account_type
            self.balance = initial_balance
            self.withdraw_count = 0
        self.account_type = account_type
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Amount must be positive')
        self.balance += amount
    
    def withdraw(self, amount):
        if self.account_type == 'Savings':
            if self.withdraw_count < 3:
                if self.balance - amount >= 1000:
                    self.balance -= amount
                    self.withdraw_count += 1
                else:
                    print("Withdrawal failed. Minimum balance requirement not met.")
            else:
                fee = 10
                if self.balance - (fee + amount) >= 1000:
                    self.balance -= (amount + fee)
                else:
                    print("Withdrawal failed. Minimum balance requirement not met.")
    
    def interest(self):
        return 0.5*self.balance if self.account_type == 'Savings' else 0.3 * self.balance

class Savings(Bank):
    def __init__(self, initial_balance) -> None:
        super().__init__('Savings', initial_balance)
    
    def calculate_interest(self):
        return self.interest()
        
class Current(Bank):
    def __init__(self, initial_balance) -> None:
        super().__init__('Current', initial_balance)
    
    def calculate_interest(self):
        return self.interest()

# Creating accounts
savings_account = Savings(1500)
current_account = Current(2000)

# Performing transactions
savings_account.withdraw(500)
current_account.deposit(1000)

# Checking balances and interest
print("Savings Account Balance:", savings_account.balance)
print("Current Account Balance:", current_account.balance)

# Calculating and displaying interest
print("Savings Account Interest:", savings_account.calculate_interest())
print("Current Account Interest:", current_account.calculate_interest())