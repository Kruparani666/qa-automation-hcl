# src/utilities/data_loader.py
import json
import pandas as pd
from typing import Dict, List, Any
import os
import logging

logger = logging.getLogger(__name__)

class DataLoader:
    """Loads test data from various sources"""
    
    @staticmethod
    def load_json(file_path: str) -> Dict[str, Any]:
        """Load data from JSON file"""
        try:
            # Handle relative paths
            if not os.path.isabs(file_path):
                # Go up 3 levels from utilities directory to project root
                project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                file_path = os.path.join(project_root, file_path)
            
            logger.info(f"Loading JSON from: {file_path}")
            
            if not os.path.exists(file_path):
                logger.warning(f"JSON file not found: {file_path}")
                return {}
            
            with open(file_path, 'r') as file:
                data = json.load(file)
            logger.info(f"Data loaded successfully from {os.path.basename(file_path)}")
            return data
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error in {file_path}: {str(e)}")
            return {}
        except Exception as e:
            logger.error(f"Error loading JSON data from {file_path}: {str(e)}")
            return {}
    
    @staticmethod
    def load_excel(file_path: str, sheet_name: str = None) -> List[Dict]:
        """Load data from Excel file"""
        try:
            # Handle relative paths
            if not os.path.isabs(file_path):
                project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                file_path = os.path.join(project_root, file_path)
            
            logger.info(f"Loading Excel from: {file_path}")
            
            if not os.path.exists(file_path):
                logger.warning(f"Excel file not found: {file_path}")
                return []
            
            if sheet_name:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
            else:
                df = pd.read_excel(file_path)
            
            # Convert to list of dictionaries
            data = df.to_dict('records')
            logger.info(f"Data loaded successfully from {os.path.basename(file_path)}")
            return data
        except Exception as e:
            logger.error(f"Error loading Excel data from {file_path}: {str(e)}")
            return []
    
    @staticmethod
    def load_test_credentials() -> List[Dict]:
        """Load test credentials"""
        from src.config.config import config
        credentials = DataLoader.load_json(config.CREDENTIALS_PATH)
        return credentials.get('users', [])
    
    @staticmethod
    def load_invalid_credentials() -> List[Dict]:
        """Load invalid credentials for negative testing"""
        from src.config.config import config
        
        # Try to load from invalid_credentials.json
        credentials_dir = os.path.dirname(config.CREDENTIALS_PATH)
        json_file = os.path.join(credentials_dir, "invalid_credentials.json")
        
        if os.path.exists(json_file):
            data = DataLoader.load_json(json_file)
            if data and isinstance(data, list):
                return data
        
        # Fallback to default test data
        logger.warning("Using default invalid credentials data")
        return [
            {"username": "invalid_user", "password": "wrong_password", "expected_error": "Invalid"},
            {"username": "test", "password": "", "expected_error": "required"},
            {"username": "", "password": "test", "expected_error": "required"}
        ]