"""
Flask application factory module.
Initializes and configures the Flask application with all its components.
"""
from flask import Flask, jsonify

def create_app() -> Flask:
    """
    Create and configure the Flask application.

    This factory function:
    - Creates the Flask instance
    - Registers blueprints for API routes
    - Sets up global 404 error handlers
    
    Returns:
        Flask: The configured Flask application instance
    """
    app = Flask(__name__)

    from app.routes.account import account_bp
    app.register_blueprint(account_bp, url_prefix='/api/accounts')
    
    @app.errorhandler(404)
    def handle_not_found_error(error) -> tuple[dict, int]:
        """
        Handle 404 Not Found errors.

        Args:
            error: The error that triggered this handler

        Returns:
            tuple: JSON response with error details and 404 status code
        """
        return jsonify({
            "error": "NOT_FOUND",
            "message": error.description
        }), 404
    
    return app 