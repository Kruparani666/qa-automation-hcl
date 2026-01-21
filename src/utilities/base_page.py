# src/utilities/base_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.config.config import config
import logging

logger = logging.getLogger(__name__)

class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = config.BASE_URL
        self.wait = WebDriverWait(driver, config.WAIT_TIME)
    
    def find_element(self, locator):
        """Find element with explicit wait"""
        try:
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element not found: {locator}")
            raise
    
    def find_elements(self, locator):
        """Find multiple elements"""
        try:
            return self.wait.until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            logger.error(f"Elements not found: {locator}")
            return []
    
    def click_element(self, locator):
        """Click element with wait"""
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return element
    
    def clear_and_send_keys(self, locator, text):
        """Clear field and enter text"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element
    
    def get_element_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return element.text.strip()
    
# In src/utilities/base_page.py - add this method
    def is_element_displayed(self, locator, timeout=10):
        """Check if element is displayed with custom timeout"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False
    
    def wait_for_element_visible(self, locator, timeout=None):
        """Wait for element to be visible"""
        timeout = timeout or config.WAIT_TIME
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def take_screenshot(self, name):
        """Take screenshot for debugging"""
        screenshot_path = f"{config.REPORT_PATH}/screenshots/{name}.png"
        self.driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path