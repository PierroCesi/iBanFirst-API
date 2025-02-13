"""
Account routes handling HTTP requests related to account operations.
"""
from flask import Blueprint, jsonify, request
from app.services.account import AccountService
from app.dto.account import AccountResponseDto
from dataclasses import asdict
from app.errors import OwnerNotFoundException, UnsupportedCurrencyException, InvalidApiKeyException

account_bp = Blueprint('account', __name__)
account_service = AccountService()

@account_bp.route('/<int:owner_id>')
def get_accounts(owner_id: int):
    """
    Get all accounts for a specific owner with optional currency conversion.

    Args:
        owner_id (int): ID of the account owner

    Query Parameters:
        currency (str, optional): Target currency for conversion

    Returns:
        JSON: List of accounts with their details
        
    Raises:
        404: When owner is not found
        400: When currency is not supported
    """
    try:
        accounts = account_service.get_accounts_by_owner(owner_id)
        target_currency = request.args.get('currency', None)

        if target_currency:
            accounts = account_service.convert_accounts_to_currency(accounts, target_currency)

        account_responses = [AccountResponseDto.from_account(account) for account in accounts]
        return jsonify(
            [asdict(response) for response in account_responses]
        )
    
    except OwnerNotFoundException as e:
        return jsonify({
            "error": "OWNER_NOT_FOUND",
            "message": str(e)
        }), 404
    
    except UnsupportedCurrencyException as e:
        return jsonify({
            "error": "UNSUPPORTED_CURRENCY",
            "message": str(e)
        }), 400

    except InvalidApiKeyException as e:
        return jsonify({
            "error": "INVALID_API_KEY",
            "message": str(e)
        }), 401