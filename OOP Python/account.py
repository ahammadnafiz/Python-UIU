# account.py
'''Account Class defination'''

from decimal import Decimal

class Account:
    '''Account Class for maintaing a bank account balance'''
    def __init__(self, name, balance) -> None:
        '''Initialize an Account object'''
        
        # if balance is less then 0 raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be greater than 0')

        self.name = name
        self.balance = balance
        
    def deposit(self, amount: float) -> float:
        """Deposit Money to the account

        Args:
            amount (float): Takes amount for deposit
        """
        
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive')
        
        self.balance += amount
    
    def withdraw(self, amount: float) -> float:
        """Withdraw money from the account

        Args:
            amount (float): withdraw amount
        """

        if amount > self.balance:
            raise ValueError('Amount must be less than Balance')
        elif amount < Decimal('0.00'):
            raise ValueError('Amount must be positive')

        self.balance -= amount