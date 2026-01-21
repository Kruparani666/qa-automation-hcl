# src/tests/test_smoke.py
import pytest
import logging
from src.config.config import config

logger = logging.getLogger(__name__)

def test_config():
    """Test that config loads correctly"""
    logger.info("Testing config...")
    assert config is not None
    assert hasattr(config, 'BASE_URL')
    assert config.BASE_URL != ""
    logger.info(f"Base URL: {config.BASE_URL}")
    assert config.BROWSER in ['chrome', 'firefox', 'edge']
    logger.info(f"Browser: {config.BROWSER}")

def test_data_loader():
    """Test data loader"""
    logger.info("Testing data loader...")
    from src.utilities.data_loader import DataLoader
    
    # Test loading credentials
    credentials = DataLoader.load_test_credentials()
    logger.info(f"Loaded {len(credentials)} credentials")
    assert isinstance(credentials, list)
    
    if credentials:
        logger.info(f"Sample credential: {credentials[0]}")

class TestSmoke:
    """Smoke tests"""
    
    @pytest.mark.smoke
    def test_simple_assertion(self):
        """Simple test to verify pytest works"""
        logger.info("Running simple assertion test")
        assert 1 + 1 == 2
    
    @pytest.mark.smoke
    def test_environment(self):
        """Test environment setup"""
        logger.info("Testing environment setup")
        from src.utilities.driver_manager import DriverManager
        
        # Just test that we can create a driver (we won't actually create it in this test)
        logger.info("DriverManager import successful")
        assert DriverManager is not None