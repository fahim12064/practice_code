import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.dailyamardesh.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(link)

wait = WebDriverWait(driver, 10)
# হেডলাইন লিংকগুলো লোড হওয়া পর্যন্ত অপেক্ষা করো
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2 a")))

# এখন সব হেডলাইন ও লিংক সংগ্রহ করো, তারপর DOM থেকে বের হয়ে যাও
elements = driver.find_elements(By.CSS_SELECTOR, "h2 a")
headlines = []

for el in elements:
    text = el.text.strip()
    href = el.get_attribute("href")
    if text and href:
        headlines.append((text, href))

driver.quit()  # ব্রাউজার বন্ধ করে দাও, এখন আর দরকার নেই

with open("amardesh_headlines.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "URL"])  # হেডার
    writer.writerows(headlines)           # ডেটা

print("✅ CSV ফাইলে সংরক্ষণ সম্পন্ন: amardesh_headlines.csv")
