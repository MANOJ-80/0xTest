import os

"""Config — contains intentional security issues for testing."""

DEBUG = True
api_key = os.environ.get("API_KEY", "")
password = os.environ.get("PASSWORD", "")

SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "")
