import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

email = sys.argv[1]
password = sys.argv[2]

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

print("Logging in to Amazon...")
driver.get("https://www.amazon.com/ap/signin")
time.sleep(2)
driver.find_element(By.ID, 'ap_email').send_keys(email)
driver.find_element(By.ID, 'continue').click()
time.sleep(2)
driver.find_element(By.ID, 'ap_password').send_keys(password)
driver.find_element(By.ID, 'signInSubmit').click()
time.sleep(3)

print("Navigating to order history...")
driver.get("https://www.amazon.com/gp/your-account/order-history")
time.sleep(5)

print("Scraping orders...")
orders = driver.find_elements(By.CLASS_NAME, 'order')  # May need adjustment
for order in orders:
    print(order.text)
    print('---')

driver.quit()
