import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'your_api_key')

# Validate that GEMINI_API_KEY is set
if GEMINI_API_KEY == 'your_api_key':
    raise ValueError(
        "GEMINI_API_KEY is not configured. "
        "Please set it in your .env file or environment variables."
    )

# Other configuration
OTHER_API_KEY = os.getenv('OTHER_API_KEY', 'your_other_api_key')