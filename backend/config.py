import os

class Config:
    """Flask application configuration"""

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///autoshop.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI API Key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-api-key")

    # Other configurations
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
