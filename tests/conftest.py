"""
Pytest configuration and fixtures.
"""
import pytest
from app import create_app
from app.services.forex import ForexService
from app.errors import UnsupportedCurrencyException
from unittest.mock import Mock

@pytest.fixture
def mock_forex_service():
    """Create a mock forex service with predefined rates."""
    mock_service = Mock(spec=ForexService)
    
    def mock_get_rates(base_currency: str, currencies: set[str]):
        if "INVALID" in currencies or base_currency == "INVALID":
            raise UnsupportedCurrencyException("INVALID")
        return {
            "USD": 1.1,
            "GBP": 0.85,
            "EUR": 1.0
        }
    
    mock_service.get_rates.side_effect = mock_get_rates
    return mock_service

@pytest.fixture
def app(mock_forex_service):
    """Create and configure a test Flask application with mocked forex service."""
    app = create_app()
    app.config['TESTING'] = True
    
    # Injecter le mock dans le service account avant de créer les routes
    from app.routes.account import account_service
    account_service.forex_service = mock_forex_service
    
    return app

@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client() 