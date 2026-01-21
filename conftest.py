# conftest.py
import pytest
import logging
from datetime import datetime
from src.utilities.driver_manager import DriverManager
from src.config.config import config

# Configure logging
def setup_logging():
    """Setup logging configuration"""
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_file = f"{config.LOG_PATH}/test_execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

@pytest.fixture(scope="session")
def logger():
    """Session-level logger fixture"""
    setup_logging()
    return logging.getLogger(__name__)

@pytest.fixture(scope="function")
def driver():
    """WebDriver fixture for each test"""
    driver = None
    try:
        driver = DriverManager.create_driver()
        yield driver
    finally:
        if driver:
            driver.quit()

@pytest.fixture(scope="function")
def login_page(driver):
    """Login page fixture"""
    from src.pages.login_page import LoginPage
    return LoginPage(driver).navigate_to_login()

@pytest.fixture(scope="function")
def forgot_password_page(driver):
    """Forgot password page fixture"""
    from src.pages.forgot_password_page import ForgotPasswordPage
    from src.pages.login_page import LoginPage
    login_page = LoginPage(driver).navigate_to_login()
    return login_page.click_forgot_password()

# Pytest hooks
def pytest_configure(config):
    """Setup pytest configuration"""
    # Add custom markers
    config.addinivalue_line(
        "markers",
        "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers",
        "regression: mark test as regression test"
    )

def pytest_html_report_title(report):
    """Set HTML report title"""
    report.title = "HCLTech Authentication Module Test Report"

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add screenshots to HTML report on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Add screenshot to report
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            try:
                screenshot_path = f"screenshots/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                driver.save_screenshot(screenshot_path)
                if hasattr(report, 'extra'):
                    report.extra.append(pytest_html.extras.image(screenshot_path))
            except:
                pass