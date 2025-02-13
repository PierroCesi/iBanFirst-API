"""
Custom exceptions.
"""

class AccountException(Exception):
    """Base exception class for account-related errors."""
    pass

class OwnerNotFoundException(AccountException):
    """
    Exception raised when an account owner is not found.
    
    Args:
        owner_id (int): ID of the owner that was not found
    """
    def __init__(self, owner_id: int) -> None:
        self.owner_id = owner_id
        self.message = f"No accounts found for owner with ID: {owner_id}"
        super().__init__(self.message)

class UnsupportedCurrencyException(AccountException):
    """
    Exception raised when a currency is not supported.
    
    Args:
        currency (str): The unsupported currency code
    """
    def __init__(self, currency: str) -> None:
        self.currency = currency
        self.message = f"Currency {currency} is not supported"
        super().__init__(self.message)

class InvalidApiKeyException(AccountException):
    """
    Exception raised when the API key is invalid or missing.
    
    Args:
        details (str, optional): Additional details about the error
    """
    def __init__(self, details: str = "Invalid or missing API key") -> None:
        self.message = details
        super().__init__(self.message) 