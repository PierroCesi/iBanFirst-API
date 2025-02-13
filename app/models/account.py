"""
Account model representing a bank account with its properties.
"""
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Account:
    """
    Data class representing a bank account.
    """
    account_id: str    # Unique identifier for the account
    balance: Decimal   # Current balance of the account
    currency: str      # Currency code (e.g., 'USD', 'EUR')
    owner_id: int      # ID of the account owner
    bank_id: int       # ID of the bank where the account is held
