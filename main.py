from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
import os
import time

# --- CONFIG ---
url = "https://www.walmart.com/ip/443574645?sid=a049bd64-95cb-49c4-a1e5-6a50e961243a"
product_name = "Xbox Series S 512 GB Console"

# --- SETUP DRIVER ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(3) # Wait for page to load

# --- GET TITLE ---
try:
title = driver.find_element(By.CSS_SELECTOR, "h1").text
except:
title = product_name # fallback

# --- GET PRICE (Updated Selector) ---
try:
price_whole = driver.find_element(By.CSS_SELECTOR, "span.price-characteristic").get_attribute("content")
price_cents = driver.find_element(By.CSS_SELECTOR, "span.price-mantissa").get_attribute("content")
price = f"${price_whole}.{price_cents}"
except:
price = "N/A"

# --- TIMESTAMP ---
date_checked = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- CLOSE DRIVER ---
driver.quit()

# --- LOG TO CSV ---
log_file = "price_log.csv"
data = {"Date": [date_checked], "Product": [title], "Price": [price]}
df = pd.DataFrame(data)

if not os.path.exists(log_file):
df.to_csv(log_file, index=False)
else:
df.to_csv(log_file, mode='a', header=False, index=False)

print(f"[✔] Logged: {title} | Price: {price} | Time: {date_checked}")