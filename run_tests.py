# run_tests.py
#!/usr/bin/env python3
"""
Test execution script for HCLTech Authentication Module
"""
import subprocess
import sys
import os
from datetime import datetime
import argparse

def run_tests(test_type="all", browser="chrome", headless=False):
    """Execute tests based on parameters"""
    
    # Create reports directory
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Set environment variables
    env = os.environ.copy()
    env["BROWSER"] = browser
    env["HEADLESS"] = str(headless)
    
    # Define pytest arguments
    pytest_args = [
        "pytest",
        f"--html={report_dir}/test_report_{timestamp}.html",
        "--self-contained-html",
        f"--junitxml={report_dir}/junit_report_{timestamp}.xml",
        "-v",
        "--tb=short",
        f"--log-cli-level=INFO"
    ]
    
    # Add markers based on test type
    if test_type == "smoke":
        pytest_args.append("-m smoke")
    elif test_type == "regression":
        pytest_args.append("-m regression")
    elif test_type == "login":
        pytest_args.append("src/tests/test_login_functionality.py")
    elif test_type == "forgot_password":
        pytest_args.append("src/tests/test_forgot_password.py")
    
    # Run tests
    print(f"\n{'='*60}")
    print(f"Running {test_type.upper()} tests")
    print(f"Browser: {browser} | Headless: {headless}")
    print(f"Timestamp: {timestamp}")
    print(f"{'='*60}\n")
    
    result = subprocess.run(pytest_args, env=env)
    
    return result.returncode

def main():
    parser = argparse.ArgumentParser(description="Run HCLTech Authentication Tests")
    parser.add_argument("--test-type", choices=["all", "smoke", "regression", "login", "forgot_password"],
                       default="all", help="Type of tests to run")
    parser.add_argument("--browser", choices=["chrome", "firefox", "edge"],
                       default="chrome", help="Browser to use for tests")
    parser.add_argument("--headless", action="store_true",
                       help="Run tests in headless mode")
    
    args = parser.parse_args()
    
    exit_code = run_tests(
        test_type=args.test_type,
        browser=args.browser,
        headless=args.headless
    )
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main()