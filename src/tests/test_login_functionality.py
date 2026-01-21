# src/tests/test_login_functionality.py - SIMPLE VERSION
import pytest
import logging
import time

logger = logging.getLogger(__name__)

class TestLoginFunctionality:
    
    @pytest.mark.smoke
    def test_valid_login_standard_user(self, login_page):
        """Test login with standard user"""
        logger.info("Testing valid login for standard_user")
        
        login_page.login(username="standard_user", password="secret_sauce")
        time.sleep(2)
        
        assert login_page.is_login_successful(), "Login failed for standard_user"
        logger.info("Successfully logged in as standard_user")
    
    @pytest.mark.smoke  
    def test_valid_login_problem_user(self, login_page):
        """Test login with problem user"""
        logger.info("Testing valid login for problem_user")
        
        login_page.login(username="problem_user", password="secret_sauce")
        time.sleep(2)
        
        assert login_page.is_login_successful(), "Login failed for problem_user"
        logger.info("Successfully logged in as problem_user")
    
    @pytest.mark.regression
    def test_invalid_login_wrong_password(self, login_page):
        """Test login with wrong password"""
        logger.info("Testing invalid login with wrong password")
        
        login_page.login(username="standard_user", password="wrong_password")
        time.sleep(1)
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error = login_page.get_error_message()
        logger.info(f"Error message: {error}")
    
    @pytest.mark.regression  
    def test_login_locked_user(self, login_page):
        """Test login with locked out user"""
        logger.info("Testing login with locked_out_user")
        
        login_page.login(username="locked_out_user", password="secret_sauce")
        time.sleep(1)
        
        assert login_page.is_error_displayed(), "Error should be displayed for locked user"
        error = login_page.get_error_message()
        assert "locked" in error.lower(), f"Expected 'locked' in error: {error}"
        logger.info(f"Locked user error: {error}")
    
    @pytest.mark.regression
    def test_login_empty_credentials(self, login_page):
        """Test login with empty credentials"""
        logger.info("Testing login with empty credentials")
        
        login_page.click_login()
        time.sleep(1)
        
        assert login_page.is_error_displayed(), "Error should be displayed for empty credentials"
        error = login_page.get_error_message()
        logger.info(f"Empty credentials error: {error}")