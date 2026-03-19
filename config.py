# Flask Configuration File

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Model parameters
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    SECRET_KEY = 'your_secret_key'

    # API settings
    API_VERSION = 'v1'
    API_PUBLIC_KEY = 'your_public_key'
    API_SECRET_KEY = 'your_secret_key'