# src/utilities/waits.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from typing import Callable, Tuple

logger = logging.getLogger(__name__)

class SmartWait:
    """Advanced wait utilities for handling dynamic elements"""
    
    def __init__(self, driver, timeout=30, poll_frequency=0.5):
        self.driver = driver
        self.timeout = timeout
        self.poll_frequency = poll_frequency
    
    def wait_for_page_load(self):
        """Wait for page to load completely"""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            logger.info("Page loaded completely")
        except TimeoutException:
            logger.warning("Page load timeout")
    
    def wait_for_element_with_retry(self, locator: Tuple, max_retries: int = 3) -> bool:
        """Wait for element with retry mechanism"""
        for attempt in range(max_retries):
            try:
                element = WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located(locator)
                )
                logger.info(f"Element found: {locator} on attempt {attempt + 1}")
                return element
            except TimeoutException:
                logger.warning(f"Element not found: {locator}, attempt {attempt + 1}")
                if attempt == max_retries - 1:
                    raise
                # Optional: Add small delay before retry
                import time
                time.sleep(1)
    
    def wait_for_element_to_disappear(self, locator: Tuple) -> bool:
        """Wait for element to disappear"""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            logger.info(f"Element disappeared: {locator}")
            return True
        except TimeoutException:
            logger.warning(f"Element still visible: {locator}")
            return False
    
    def wait_for_text_to_be_present(self, locator: Tuple, text: str) -> bool:
        """Wait for specific text to be present in element"""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            logger.info(f"Text '{text}' found in element: {locator}")
            return True
        except TimeoutException:
            logger.warning(f"Text '{text}' not found in element: {locator}")
            return False
    
    def wait_for_ajax_complete(self):
        """Wait for AJAX calls to complete (jQuery specific)"""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                lambda d: d.execute_script("return jQuery.active == 0")
            )
            logger.info("AJAX calls completed")
        except:
            # jQuery might not be present, ignore
            pass