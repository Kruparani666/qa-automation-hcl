HCLTech QA Automation Framework - Authentication Module
📋 Overview
A comprehensive test automation framework for web application authentication modules, developed as per HCLTech's enterprise QA standards. This framework demonstrates industry-best practices in test automation for login and password reset functionalities.

🎯 Project Purpose
This project simulates a real-world enterprise QA automation scenario for HCLTech, testing web application authentication features including login functionality, error validations, and password reset workflows.

✨ Features
Page Object Model (POM) architecture for maintainable test code

Data-Driven Testing with JSON configuration

Cross-Browser Support (Chrome, Firefox, Edge)

Comprehensive Reporting (HTML, XML, logs)

Parallel Test Execution support

Headless Mode for CI/CD pipelines

Smart Element Waiting and synchronization

Screenshot Capture on test failures

📁 Project Structure
text
qa-automation-hcl/
├── src/
│   ├── pages/               # Page Object Classes
│   │   ├── login_page.py
│   │   └── forgot_password_page.py
│   ├── tests/              # Test Suites
│   │   ├── test_login_functionality.py
│   │   ├── test_forgot_password.py
│   │   └── test_smoke.py
│   ├── utilities/          # Helper Classes
│   │   ├── base_page.py
│   │   ├── driver_manager.py
│   │   ├── data_loader.py
│   │   └── waits.py
│   └── config/            # Configuration
│       └── config.py
├── data/                  # Test Data
│   ├── credentials.json
│   └── invalid_credentials.json
├── reports/              # Test Reports
│   └── screenshots/     # Failure screenshots
├── logs/                # Execution Logs
├── conftest.py          # Pytest Fixtures
├── requirements.txt     # Dependencies
├── run_tests.py        # Test Runner
├── setup_data.py       # Data Setup Script
└── README.md           # This file
🛠️ Prerequisites
Python 3.8+

Chrome/Firefox/Edge browser installed

Internet connection (for SauceDemo testing)

⚙️ Installation
1. Clone/Setup the Project
bash
# Create and navigate to project directory
mkdir qa-automation-hcl
cd qa-automation-hcl

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
2. Install Dependencies
bash
pip install -r requirements.txt
3. Setup Test Data
bash
python setup_data.py
🚀 Usage
Running All Tests
bash
python run_tests.py
Run Specific Test Types
bash
# Run smoke tests
python run_tests.py --test-type smoke

# Run regression tests
python run_tests.py --test-type regression

# Run login tests only
python run_tests.py --test-type login

# Run forgot password tests only
python run_tests.py --test-type forgot_password
Browser Options
bash
# Run with Chrome (default)
python run_tests.py --browser chrome

# Run with Firefox
python run_tests.py --browser firefox

# Run with Edge
python run_tests.py --browser edge
Headless Mode (for CI/CD)
bash
python run_tests.py --headless
Custom Configuration
bash
# Run smoke tests in headless Firefox
python run_tests.py --test-type smoke --browser firefox --headless

# Run regression tests with Chrome in headless mode
python run_tests.py --test-type regression --headless
🧪 Test Coverage
Authentication Features Tested:
Login Functionality

Valid credentials login

Invalid credentials handling

Empty credentials validation

Locked user account handling

Error message validations

Password Reset Workflow (Mock Implementation)

Navigation to forgot password

Valid email submission

Invalid email validation

Empty email handling

Cancel operation

Test Types:
Smoke Tests: Critical functionality verification

Regression Tests: Comprehensive feature validation

Negative Tests: Error handling and edge cases

📊 Test Reports
Generated Reports:
HTML Report: reports/test_report_{timestamp}.html

Interactive dashboard

Test results with pass/fail status

Execution times

Error details

JUnit XML Report: reports/junit_report_{timestamp}.xml

CI/CD integration ready

Standardized format

Execution Logs: logs/test_execution_{timestamp}.log

Detailed step-by-step execution

Debug information

Error stack traces

Screenshots: reports/screenshots/

Automatic capture on test failures

Helpful for debugging

Viewing Reports:
bash
# Open HTML report in default browser (Windows)
start reports\test_report_*.html

# Open HTML report (Mac)
open reports/test_report_*.html

# Open HTML report (Linux)
xdg-open reports/test_report_*.html
⚙️ Configuration
Environment Variables:
bash
# Application URL (default: https://www.saucedemo.com)
set APP_URL=https://your-app-url.com

# Browser selection (chrome, firefox, edge)
set BROWSER=firefox

# Headless mode (true/false)
set HEADLESS=true

# Timeout settings
set TIMEOUT=30
set WAIT_TIME=10
Configuration File: src/config/config.py
python
BASE_URL = "https://www.saucedemo.com"  # Test application
BROWSER = "chrome"                      # Default browser
HEADLESS = False                        # Headless mode
TIMEOUT = 30                            # Global timeout
WAIT_TIME = 10                          # Default wait time
📝 Test Data Management
Sample Test Data: data/credentials.json
json
{
  "users": [
    {
      "username": "standard_user",
      "password": "secret_sauce",
      "role": "standard",
      "remember_me": true
    }
  ],
  "password_reset_emails": [
    "test@example.com"
  ]
}
Invalid Credentials: data/invalid_credentials.json
json
[
  {
    "username": "invalid_user",
    "password": "wrong_password",
    "expected_error": "Invalid username or password"
  }
]
🏗️ Framework Architecture
1. Page Object Model (POM)
LoginPage: Handles all login page interactions

ForgotPasswordPage: Manages password reset functionality

BasePage: Common utilities and base methods

2. Test Structure
Modular test classes

Data-driven test methods

Fixtures for setup/teardown

Custom markers for test categorization

3. Utilities
DriverManager: Browser automation setup

DataLoader: Test data management

SmartWait: Advanced synchronization

BasePage: Common web element interactions

🔧 Customization
Adding New Tests
Create new test methods in existing test classes

Add new test data in JSON files

Use custom markers for test categorization

Implement new page objects for additional features

Extending the Framework
Add new browser support in driver_manager.py

Implement custom reporting formats

Add API testing capabilities

Integrate with test management tools

🐛 Troubleshooting
Common Issues:
Browser Driver Issues

bash
# Install ChromeDriver manually
pip install chromedriver-autoinstaller

# Or update webdriver_manager
pip install --upgrade webdriver-manager
Import Errors

bash
# Ensure Python path is set
set PYTHONPATH=%cd%

# Check virtual environment activation
venv\Scripts\activate
Test Failures

Check network connectivity

Verify test application is accessible

Review logs in logs/ directory

Check screenshots in reports/screenshots/

Debug Mode:
bash
# Run with verbose logging
pytest -v --log-cli-level=DEBUG

# Run single test for debugging
pytest src/tests/test_login_functionality.py::TestLoginFunctionality::test_valid_login_standard_user -v
📈 Best Practices Implemented
Code Quality
PEP 8 compliance

Comprehensive docstrings

Type hints for better IDE support

Meaningful variable/method names

Test Design
Independent test cases

Proper setup/teardown

Data-driven approach

Reusable test utilities

Maintenance
Centralized configuration

Externalized test data

Comprehensive logging

Automatic reporting

🤝 Contributing
Fork the repository

Create a feature branch

Add tests for new functionality

Ensure all tests pass

Submit a pull request

📄 License
This project is developed for educational and demonstration purposes as part of HCLTech QA automation case study.

🙏 Acknowledgments
Test application: SauceDemo

Selenium WebDriver for browser automation

Pytest framework for test execution

HCLTech for the comprehensive case study requirements

📞 Support
For issues or questions:

Check the logs/ directory for detailed error information

Review generated screenshots for visual debugging

Examine test reports for execution details

Refer to this README for configuration guidance
