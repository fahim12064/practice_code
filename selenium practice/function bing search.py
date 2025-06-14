from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv

def launch_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.bing.com/")
    sleep(3)
    return driver

def perform_search(driver, query):
    search_q = driver.find_element(By.ID, "sb_form_q")
    search_q.send_keys(query)
    search_q.send_keys(Keys.RETURN)
    sleep(5)

def scrape_results(driver, writer):
    links = driver.find_elements(By.CSS_SELECTOR, "li.b_algo h2 a")
    for link in links:
        url = link.get_attribute('href')
        name = link.text
        if url and "youtube.com" not in url:
            print(f"{name} = {url}")
            writer.writerow([name, url])

def go_to_next_page(driver):
    try:
        next_button = driver.find_element(By.XPATH, '//a[@title="Next page"]')
        next_button.click()
        sleep(3)
        return True
    except:
        print("There is no more page.")
        return False

def close_browser(driver):
    driver.quit()

def bing_search_scraper(query, target_page=5, output_file="bing_search_results.csv"):
    driver = launch_browser()
    perform_search(driver, query)

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "URL"])

        current_page = 1
        while current_page <= target_page:
            print(f"\n--- Page {current_page} ---")
            scrape_results(driver, writer)
            if not go_to_next_page(driver):
                break
            current_page += 1

    close_browser(driver)


# Function call example:
bing_search_scraper("prompt engineering free course", target_page=15, output_file="bing_search_results2.csv")
