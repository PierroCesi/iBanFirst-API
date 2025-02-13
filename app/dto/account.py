"""
Data Transfer Objects for account-related operations.
"""
from dataclasses import dataclass
from app.models.account import Account
from decimal import Decimal

@dataclass
class AccountResponseDto:
    """
    DTO for sending account information in API responses.
    Provides a private view of an account, excluding sensitive or internal data.
    """
    account_id: str  # Unique identifier of the account
    currency: str    # Currency code of the account (e.g., 'USD', 'EUR')
    balance: Decimal # Current balance of the account
    owner_id: int    # ID of the account owner

    @classmethod
    def from_account(cls, account: Account) -> 'AccountResponseDto':
        """
        Create an AccountResponse DTO from an Account model.

        Args:
            account (Account): The account model to convert

        Returns:
            AccountResponse: The DTO representation of the account
        """
        return cls(
            account_id=account.account_id,
            currency=account.currency,
            balance=account.balance,
            owner_id=account.owner_id
        ) 