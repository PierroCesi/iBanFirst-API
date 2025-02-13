"""
Tests for the account API routes.
"""
import pytest
from unittest.mock import patch
from app.services.forex import ForexService

def test_unknown_url(client):
    """Test 404 response when URL is not found."""
    response = client.get('/api/unknown')

    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'NOT_FOUND'

def test_get_accounts_success(client):
    """Test successful retrieval of accounts."""
    response = client.get('/api/accounts/12')
    
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(
        all(key in account for key in ['account_id', 'balance', 'currency', 'owner_id'])
        for account in data
    )

def test_get_accounts_owner_not_found(client):
    """Test 404 response when owner is not found."""
    response = client.get('/api/accounts/999')
    
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'OWNER_NOT_FOUND'

def test_get_accounts_with_currency_conversion(client):
    """Test accounts retrieval with currency conversion."""
    response = client.get('/api/accounts/12?currency=EUR')
    
    assert response.status_code == 200
    data = response.get_json()
    assert all(account['currency'] == 'EUR' for account in data)

def test_get_accounts_invalid_currency(client):
    """Test error handling for invalid currency."""
    response = client.get('/api/accounts/12?currency=INVALID')
    
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'UNSUPPORTED_CURRENCY'
