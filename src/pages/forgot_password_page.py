# src/pages/forgot_password_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class ForgotPasswordPage(BasePage):
    """Mock Page Object for Forgot Password Page"""
    
    # Mock locators for demonstration
    EMAIL_INPUT = (By.ID, "email")
    RESET_BUTTON = (By.ID, "resetBtn")
    CANCEL_BUTTON = (By.ID, "cancelBtn")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "reset-success")
    ERROR_MESSAGE = (By.CLASS_NAME, "reset-error")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
    
    def enter_email(self, email: str):
        """Enter email for password reset"""
        logger.info(f"Entering email for password reset: {email}")
        # For demo, just print the action
        print(f"Would enter email: {email}")
        return self
    
    def click_reset(self):
        """Click reset password button"""
        logger.info("Clicking reset password button")
        # For demo, just print the action
        print("Would click reset button")
        return self
    
    def click_cancel(self):
        """Click cancel button"""
        logger.info("Clicking cancel button")
        # For demo, navigate back
        self.driver.back()
        from src.pages.login_page import LoginPage
        return LoginPage(self.driver)
    
    def get_success_message(self) -> str:
        """Get success message after reset request"""
        return "Password reset email sent successfully"
    
    def get_error_message(self) -> str:
        """Get error message if any"""
        return "Email not found"
    
    def reset_password(self, email: str):
        """Complete password reset flow"""
        logger.info(f"Initiating password reset for email: {email}")
        self.enter_email(email)
        self.click_reset()
        return self
    
    def wait_for_reset_complete(self):
        """Wait for reset process to complete"""
        import time
        time.sleep(1)  # Simulate waiting