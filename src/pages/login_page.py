# src/pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    """Page Object for Login Page - SauceDemo"""
    
    # SauceDemo specific locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    SUCCESS_INDICATOR = (By.CLASS_NAME, "app_logo")  # After login success
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to_login(self):
        """Navigate to login page"""
        logger.info("Navigating to login page")
        self.driver.get(f"{self.base_url}")
        self.wait_for_page_load()
        return self
    
    def enter_username(self, username: str):
        """Enter username in the username field"""
        logger.info(f"Entering username: {username}")
        self.clear_and_send_keys(self.USERNAME_INPUT, username)
        return self
    
    def enter_password(self, password: str):
        """Enter password in the password field"""
        logger.info("Entering password")
        self.clear_and_send_keys(self.PASSWORD_INPUT, password)
        return self
    
    def click_login(self):
        """Click login button"""
        logger.info("Clicking login button")
        self.click_element(self.LOGIN_BUTTON)
        return self
    
    def get_error_message(self) -> str:
        """Get error message text"""
        logger.info("Retrieving error message")
        return self.get_element_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.is_element_displayed(self.ERROR_MESSAGE)
    
    def is_login_successful(self) -> bool:
        """Check if login was successful"""
        logger.info("Checking if login was successful")
        try:
            # Check for products page or menu button after login
            return self.is_element_displayed(self.MENU_BUTTON) or \
                   self.is_element_displayed(self.SUCCESS_INDICATOR)
        except:
            return False
    
    def login(self, username: str, password: str):
        """Complete login flow"""
        logger.info(f"Attempting login with username: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self
    
    def wait_for_page_load(self):
        """Wait for login page to load completely"""
        self.wait.until(
            EC.presence_of_element_located(self.LOGIN_BUTTON)
        )