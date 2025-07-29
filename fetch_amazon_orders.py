import sys
import time
import tempfile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Get email and password from command-line arguments
email = sys.argv[1]
password = sys.argv[2]

# Set Chrome options
options = Options()
# Visible browser for debugging (comment out if using headless)
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

# Set Chrome binary location — adjust if using Google Chrome instead of Chromium
options.binary_location = "/usr/bin/chromium-browser"

# Use a unique temporary user data directory to avoid session errors
user_data_dir = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={user_data_dir}")

# Create a unique temp profile directory
profile_path = tempfile.mkdtemp(prefix="selenium-profile-")
options.add_argument(f"--user-data-dir={profile_path}")

# Start Chrome driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    print("[*] Navigating to Amazon login...")
    driver.get("https://www.amazon.com/ap/signin")

    # Wait for email field
    email_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "ap_email"))
    )
    email_input.send_keys(email)
    driver.find_element(By.ID, "continue").click()

    # Wait for password field
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "ap_password"))
    )
    password_input.send_keys(password)
    driver.find_element(By.ID, "signInSubmit").click()

    # Wait for redirect or login
    time.sleep(5)

    print("[*] Navigating to order history...")
    driver.get("https://www.amazon.com/gp/your-account/order-history")
    time.sleep(5)

    orders = driver.find_elements(By.CSS_SELECTOR, ".order")

    if not orders:
        print("[!] No orders found or not logged in successfully.")
    else:
        print("[+] Orders:")
        for order in orders:
            print(order.text)
            print("-" * 40)

except TimeoutException:
    print("[!] Timeout waiting for Amazon login or order page.")
except Exception as e:
    print(f"[!] Unexpected error: {e}")
finally:
    input("\nPress Enter to close browser...")
    driver.quit()
