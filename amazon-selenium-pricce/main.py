from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import requests
from win10toast import ToastNotifier

# Create a ToastNotifier object
toaster = ToastNotifier()

# Send a notification
toaster.show_toast("Notification", "Starting the script...")

options = Options()
# options.add_argument("--headless")

# Set up proxy
proxy_host = "50.172.75.126"
proxy_port = "80"

options.add_argument(f"--proxy-server={proxy_host}:{proxy_port}")

user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"

with open("amazon-selenium-pricce/products.txt") as f:
    products = f.readlines()

driver = webdriver.Chrome(options=options)

for product in products:
    driver.get(product)
    import time
    time.sleep(5)
