import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Read credentials from command-line args
email = sys.argv[1]
password = sys.argv[2]

# Set Chrome options for headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Use webdriver-manager to auto-install the right ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Go to Amazon login page
driver.get("https://www.amazon.com/ap/signin")
time.sleep(2)

driver.find_element(By.ID, "ap_email").send_keys(email)
driver.find_element(By.ID, "continue").click()
time.sleep(2)

driver.find_element(By.ID, "ap_password").send_keys(password)
driver.find_element(By.ID, "signInSubmit").click()
time.sleep(5)

# Go to order history
driver.get("https://www.amazon.com/gp/your-account/order-history")
time.sleep(5)

# Find and print orders
orders = driver.find_elements(By.CSS_SELECTOR, ".order")
for order in orders:
    print(order.text)
    print("-" * 40)

driver.quit()
