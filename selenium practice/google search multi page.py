import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
import random

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")
sleep(random.uniform(2, 4))

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("best prompt engineering course free")
sleep(random.uniform(1, 2))
search_box.submit()

sleep(5)  # wait for results to load

def get_links():
    results = driver.find_elements(By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md")
    links = []
    for h3 in results:
        try:
            parent_a = h3.find_element(By.XPATH, "./ancestor::a")
            title = h3.text
            link = parent_a.get_attribute("href")
            links.append((title, link))
        except Exception as e:
            print("Could not find link:", e)
    return links

all_links = []

# Get links from first page
all_links.extend(get_links())

# Try to go to the next page and get links there
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "pnnext"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    sleep(1)
    driver.execute_script("arguments[0].click();", next_button)
    sleep(random.uniform(3, 5))  # wait for next page to load

    all_links.extend(get_links())

except (TimeoutException, NoSuchElementException):
    print("Next page not found or cannot click.")

# Save to CSV
with open('google_search_links.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Link'])
    writer.writerows(all_links)

print(f"Saved {len(all_links)} links to google_search_links.csv")

driver.quit()
