# setup_data.py
import json
import os

def create_test_data():
    """Create test data files"""
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Create credentials.json
    credentials_data = {
        "users": [
            {
                "username": "standard_user",
                "password": "secret_sauce",
                "role": "standard",
                "remember_me": True
            },
            {
                "username": "admin_user", 
                "password": "admin123",
                "role": "admin",
                "remember_me": False
            }
        ],
        "password_reset_emails": [
            "valid.user@hcltech.com",
            "admin@hcltech.com"
        ]
    }
    
    with open("data/credentials.json", "w") as f:
        json.dump(credentials_data, f, indent=2)
    print("Created data/credentials.json")
    
    # Create invalid_credentials.json
    invalid_credentials_data = [
        {
            "username": "invalid_user",
            "password": "wrong_password", 
            "expected_error": "Invalid username or password"
        },
        {
            "username": "locked_user",
            "password": "secret_sauce",
            "expected_error": "User account is locked"
        },
        {
            "username": "",
            "password": "secret_sauce",
            "expected_error": "Username is required"
        },
        {
            "username": "standard_user",
            "password": "",
            "expected_error": "Password is required"
        }
    ]
    
    with open("data/invalid_credentials.json", "w") as f:
        json.dump(invalid_credentials_data, f, indent=2)
    print("Created data/invalid_credentials.json")
    
    # Create a sample test_data.xlsx placeholder
    print("\nNote: test_data.xlsx is not created as it requires pandas and openpyxl")
    print("The code will use JSON files instead.")
    
    print("\nData files created successfully!")

if __name__ == "__main__":
    create_test_data()