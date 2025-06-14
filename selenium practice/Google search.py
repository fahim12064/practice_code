from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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

# সব result এর <h3> ট্যাগ যেখানে class="LC20lb MBeuO DKV0Md" আছে, সেগুলো নিয়ে আসা
results = driver.find_elements(By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md")

for h3 in results:
    try:
        # h3 এর প্যারেন্ট <a> ট্যাগ থেকে লিংক নিয়ে আসা
        parent_a = h3.find_element(By.XPATH, "./ancestor::a")
        title = h3.text
        link = parent_a.get_attribute("href")
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("-" * 50)
    except Exception as e:
        print("Link খুঁজে পাওয়া যায়নি:", e)

driver.quit()
