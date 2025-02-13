"""
Tests for the account model.
"""
from app.models.account import Account
from decimal import Decimal

def test_account_creation():
    """Test account model creation with all required fields."""
    account = Account(
        account_id="test-id",
        balance=Decimal('100.00'),
        currency="USD",
        owner_id=1,
        bank_id=1
    )
    
    assert account.account_id == "test-id"
    assert account.balance == Decimal('100.00')
    assert account.currency == "USD"
    assert account.owner_id == 1
    assert account.bank_id == 1 