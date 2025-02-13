"""
Service layer for account management.
Handles business logic related to accounts including currency conversion.
"""
from app.models.account import Account
from app.errors import OwnerNotFoundException
from app.services.forex import ForexService
from decimal import Decimal

class AccountService:
    """
    Service class for managing accounts and their operations.
    Provides methods for retrieving and converting account currencies.
    """

    def __init__(self) -> None:
        """Initialize the account service with static data and forex service."""
        self.forex_service = ForexService()
        
        self.accounts = [
            Account(
                account_id="26fd0587-a",
                balance=Decimal('3601.03'),
                currency="USD",
                owner_id=12,
                bank_id=1
            ),
            Account(
                account_id="8762d05f-b",
                balance=Decimal('1014.00'),
                currency="GBP",
                owner_id=12,
                bank_id=3
            ),
            Account(
                account_id="072865fd-a",
                balance=Decimal('10442.45'),
                currency="USD",
                owner_id=10,
                bank_id=1
            ),
            Account(
                account_id="287605fd-d",
                balance=Decimal('5088.10'),
                currency="EUR",
                owner_id=12,
                bank_id=2
            )
        ]

    def get_accounts_by_owner(self, owner_id: int) -> list[Account]:
        """
        Retrieve all accounts for a specific owner.

        Args:
            owner_id (int): The ID of the account owner

        Returns:
            list[Account]: List of accounts belonging to the owner

        Raises:
            OwnerNotFoundException: If no accounts are found for the owner
        """
        accounts = [account for account in self.accounts if account.owner_id == owner_id]
        if not accounts:
            raise OwnerNotFoundException(owner_id)
        return accounts

    def convert_accounts_to_currency(self, accounts: list[Account], target_currency: str) -> list[Account]:
        """
        Convert a list of accounts to a target currency.

        Args:
            accounts (list[Account]): List of accounts to convert
            target_currency (str): Target currency code (e.g., 'USD', 'EUR')

        Returns:
            list[Account]: New list of accounts with converted balances.
        """
        if not target_currency:
            return accounts

        source_currencies = {account.currency for account in accounts if account.currency != target_currency}
        if not source_currencies:
            return accounts

        rates = self.forex_service.get_rates(base_currency=target_currency, currencies=source_currencies)

        return [
            Account(
                account_id=account.account_id,
                balance=(
                    account.balance 
                    if account.currency == target_currency
                    else (account.balance / Decimal(rates[account.currency])).quantize(Decimal('0.01'))
                ),
                currency=target_currency,
                owner_id=account.owner_id,
                bank_id=account.bank_id
            )
            for account in accounts
        ]
        
