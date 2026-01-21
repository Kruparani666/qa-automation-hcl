# src/utilities/driver_manager.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from src.config.config import config
import logging
import os

logger = logging.getLogger(__name__)

class DriverManager:
    """Manages WebDriver instances"""
    
    @staticmethod
    def create_driver():
        """Create and configure WebDriver instance"""
        browser = config.BROWSER.lower()
        driver = None
        
        try:
            if browser == "chrome":
                options = webdriver.ChromeOptions()
                if config.HEADLESS:
                    options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--disable-gpu")
                options.add_argument("--disable-extensions")
                
                # Fix: Use a specific ChromeDriver version instead of auto-detecting
                # This avoids PowerShell dependency for browser detection
                try:
                    # Try to use webdriver_manager with specific version
                    from webdriver_manager.core.os_manager import ChromeType
                    service = ChromeService(ChromeDriverManager().install())
                except Exception as e:
                    logger.warning(f"webdriver_manager failed: {e}. Trying fallback...")
                    # Fallback: Use ChromeDriver from PATH or specify path
                    service = ChromeService()
                
                driver = webdriver.Chrome(service=service, options=options)
                
            elif browser == "firefox":
                options = webdriver.FirefoxOptions()
                if config.HEADLESS:
                    options.add_argument("--headless")
                try:
                    service = FirefoxService(GeckoDriverManager().install())
                except Exception as e:
                    logger.warning(f"webdriver_manager failed: {e}. Trying fallback...")
                    service = FirefoxService()
                driver = webdriver.Firefox(service=service, options=options)
                
            elif browser == "edge":
                options = webdriver.EdgeOptions()
                if config.HEADLESS:
                    options.add_argument("--headless")
                try:
                    service = EdgeService(EdgeChromiumDriverManager().install())
                except Exception as e:
                    logger.warning(f"webdriver_manager failed: {e}. Trying fallback...")
                    service = EdgeService()
                driver = webdriver.Edge(service=service, options=options)
                
            else:
                raise ValueError(f"Unsupported browser: {browser}")
            
            # Common configurations
            driver.implicitly_wait(config.WAIT_TIME)
            driver.set_page_load_timeout(config.TIMEOUT)
            driver.maximize_window()
            logger.info(f"{browser.capitalize()} driver initialized successfully")
            
            return driver
            
        except Exception as e:
            logger.error(f"Failed to initialize driver: {str(e)}")
            # Provide helpful troubleshooting info
            logger.error("\nTROUBLESHOOTING:")
            logger.error("1. Make sure you have Chrome/Firefox/Edge installed")
            logger.error("2. Try installing Chrome from: https://www.google.com/chrome/")
            logger.error("3. Or use headless mode with: --headless")
            logger.error("4. Or try Firefox: --browser firefox")
            raise