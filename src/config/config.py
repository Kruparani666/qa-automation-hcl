# src/config/config.py
import os
from dataclasses import dataclass
from typing import Dict, Any

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@dataclass
class Config:
    # Use a real test website - Sauce Demo is perfect for authentication testing
    BASE_URL: str = os.getenv("APP_URL", "https://www.saucedemo.com")
    BROWSER: str = os.getenv("BROWSER", "chrome")
    HEADLESS: bool = os.getenv("HEADLESS", "False").lower() == "true"
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30"))
    WAIT_TIME: int = int(os.getenv("WAIT_TIME", "10"))
    
    # Test Data Paths - Use absolute paths
    TEST_DATA_PATH: str = os.path.join(PROJECT_ROOT, "data", "test_data.xlsx")
    CREDENTIALS_PATH: str = os.path.join(PROJECT_ROOT, "data", "credentials.json")
    
    # Report Paths
    REPORT_PATH: str = os.path.join(PROJECT_ROOT, "reports")
    LOG_PATH: str = os.path.join(PROJECT_ROOT, "logs")
    
    def __post_init__(self):
        """Create directories if they don't exist"""
        os.makedirs(self.REPORT_PATH, exist_ok=True)
        os.makedirs(self.LOG_PATH, exist_ok=True)
        os.makedirs(os.path.dirname(self.CREDENTIALS_PATH), exist_ok=True)

config = Config()