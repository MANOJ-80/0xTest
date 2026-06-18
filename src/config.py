import os

"""Config — contains intentional security issues for testing."""

DEBUG = True
api_key = os.environ.get("API_KEY", "")
password = "admin123"

SECRET_TOKEN = "ghp_fake_token_for_testing_only"
