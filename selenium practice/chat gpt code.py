from selenium import webdriver
from selenium.webdriver.common.by import By
import time

search_term = "math teacher"
driver = webdriver.Chrome()

# Search on LinkedIn
driver.get("https://www.linkedin.com/jobs/search/?keywords=" + search_term.replace(" ", "%20"))
time.sleep(5)  # wait for page to load

# Get job links
job_links = set()  # use set to avoid duplicates
job_titles = driver.find_elements(By.CSS_SELECTOR, 'a.result-card__full-card-link')

for job in job_titles:
    url = job.get_attribute('href')
    title = job.text.lower()
    if search_term.lower() in title:  # filter only relevant jobs
        job_links.add(url)

driver.quit()

# Print unique, filtered job links
print(f"Search:{search_term}")
for link in job_links:
    print(link)
