from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv

# Launch Chrome
driver = webdriver.Chrome()
driver.get("https://www.bing.com/")
sleep(3)

# Search Query
search_q = driver.find_element(By.ID, "sb_form_q")
search_q.send_keys("prompt engineering free course")
search_q.send_keys(Keys.RETURN)
sleep(5)

# CSV file creation
with open("bing_search_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL"])

    current_page = 1
    target_page = 5

    while current_page <= target_page:
        print(f"\n--- Page {current_page} ---")

        # Scrape all links
        links = driver.find_elements(By.CSS_SELECTOR, "li.b_algo h2 a")
        for link in links:
            url = link.get_attribute('href')
            name = link.text
            if url and "youtube.com" not in url:
                print(f"{name} = {url}")
                writer.writerow([name, url])

        # Try to go to next page
        try:
            next_button = driver.find_element(By.XPATH, '//a[@title="Next page"]')
            next_button.click()
            current_page += 1
            sleep(3)
        except:
            print("There is no more page.")
            break

# Close browser
driver.quit()
