import sys
import time
import os
import shutil
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Arguments
email = sys.argv[1]
password = sys.argv[2]

# Unique user data directory
profile_dir = f"/tmp/chrome-profile-{uuid.uuid4()}"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_argument(f"--user-data-dir={profile_dir}")
options.binary_location = "/usr/bin/chromium-browser"

print(f"[INFO] Using Chrome profile: {profile_dir}")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.amazon.com/ap/signin")
    time.sleep(2)
    driver.find_element(By.ID, "ap_email").send_keys(email)
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    driver.find_element(By.ID, "ap_password").send_keys(password)
    driver.find_element(By.ID, "signInSubmit").click()
    time.sleep(5)

    driver.get("https://www.amazon.com/gp/your-account/order-history")
    time.sleep(5)

    orders = driver.find_elements(By.CSS_SELECTOR, ".order")
    for order in orders:
        print(order.text)
        print("-" * 40)

finally:
    driver.quit()
    print(f"[CLEANUP] Removing temp profile: {profile_dir}")
    shutil.rmtree(profile_dir, ignore_errors=True)
