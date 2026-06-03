import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key-for-dev')
    DEBUG = True
    # Add other configuration variables here as needed
