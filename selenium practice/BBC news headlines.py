from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome চালু করা
driver = webdriver.Chrome()

driver.get("https://www.bbc.com/")
driver.maximize_window()

# অপেক্ষা করা headline link লোড হওয়া পর্যন্ত
wait = WebDriverWait(driver, 10)
links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-testid="internal-link"]')))

# শিরোনাম প্রিন্ট করা (সর্বোচ্চ 10টা)
for link in links[:10]:
    title = link.text.strip()
    url = link.get_attribute("href")
    print(f"{title} - {url}")

driver.quit()
