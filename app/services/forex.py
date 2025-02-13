"""
Service for handling currency exchange operations via Forex Rate API.
"""
import os
import requests
from typing import Dict
from app.errors import UnsupportedCurrencyException, InvalidApiKeyException

class ForexService:
    """
    Service class for currency exchange operations.
    Handles API calls to the Forex Rate API service.
    """

    def __init__(self, api_key: str = None) -> None:
        """Initialize the forex service with API configuration."""
        self.api_key = api_key or os.getenv('FOREX_API_KEY')
        self.base_url = "https://api.forexrateapi.com/v1/latest"

    def get_rates(self, base_currency: str, currencies: set[str]) -> Dict[str, float]:
        """
        Get exchange rates for multiple currencies.

        Args:
            base_currency (str): Base currency code (e.g., 'USD', 'EUR')
            currencies (set[str]): Set of currency codes to get rates for

        Returns:
            Dict[str, float]: Dictionary mapping currency codes to their exchange rates

        Raises:
            UnsupportedCurrencyException: If a currency is not supported
            InvalidApiKeyException: If the API key is invalid
            Exception: If there's an API error
        """
        try:
            if not currencies:
                return {}

            currencies_param = ",".join(currencies)
            response = requests.get(
                f"{self.base_url}?api_key={self.api_key}&base={base_currency}&currencies={currencies_param}"
            )
            data = response.json()
            
            if not data.get("success"):
                error = data.get("error", {})
                if error.get("statusCode") == 102:
                    raise InvalidApiKeyException(error.get("message"))
                raise UnsupportedCurrencyException(base_currency)
            
            return data.get("rates", {})
            
        except requests.RequestException as error:
            raise Exception(f"Error fetching exchange rates: {error}")

