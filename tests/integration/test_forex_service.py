import pytest
import os
from app.services.forex import ForexService
from app.errors import InvalidApiKeyException
from dotenv import load_dotenv

@pytest.mark.integration
def test_forex_api_integration():
    """Test real API call to forex service."""
    load_dotenv()
    
    api_key = os.getenv('FOREX_API_KEY')
    if not api_key:
        pytest.skip("FOREX_API_KEY not found in environment")

    service = ForexService()
    rates = service.get_rates("EUR", {"USD", "GBP"})
    
    assert isinstance(rates, dict)
    assert "USD" in rates
    assert "GBP" in rates 

@pytest.mark.integration
def test_forex_api_invalid_key():
    """Test API authentication error."""
    service = ForexService("invalid_key")
    with pytest.raises(InvalidApiKeyException):
        service.get_rates("EUR", {"USD", "GBP"})
