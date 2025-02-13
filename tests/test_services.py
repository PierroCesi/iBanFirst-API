"""
Tests for account and forex services.
"""
import pytest
from app.services.account import AccountService
from app.errors import OwnerNotFoundException, UnsupportedCurrencyException

def test_get_accounts_by_owner_success(mock_forex_service):
    """Test successful retrieval of accounts by owner."""
    service = AccountService()
    service.forex_service = mock_forex_service
    
    accounts = service.get_accounts_by_owner(12)
    assert len(accounts) == 3
    assert all(account.owner_id == 12 for account in accounts)

def test_get_accounts_by_owner_not_found():
    """Test owner not found scenario."""
    service = AccountService()
    
    with pytest.raises(OwnerNotFoundException) as exc:
        service.get_accounts_by_owner(999)
    assert "999" in str(exc.value)

def test_convert_accounts_currency_success(mock_forex_service):
    """Test successful currency conversion of accounts."""
    service = AccountService()
    service.forex_service = mock_forex_service
    
    accounts = service.get_accounts_by_owner(12)
    converted = service.convert_accounts_to_currency(accounts, "EUR")
    
    assert all(account.currency == "EUR" for account in converted) 