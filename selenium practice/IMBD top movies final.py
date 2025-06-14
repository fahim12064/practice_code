import re
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top/")

movies = {}

divs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item"))
)

for div in divs:
    name_element = div.find_element(By.CSS_SELECTOR, "h3.ipc-title__text")
    raw_name = name_element.text.strip()
    movie_name = re.sub(r'^\d+\.\s*', '', raw_name)

    # Meta Data
    meta_data = div.find_elements(By.CSS_SELECTOR, 'span.sc-4b408797-8.iurwGb.cli-title-metadata-item')
    year = meta_data[0].text if len(meta_data) > 0 else "N/A"
    length = meta_data[1].text if len(meta_data) > 1 else "N/A"
    certificate = meta_data[2].text if len(meta_data) > 2 else "N/A"

    # ✅ Rating per movie (from div)
    try:
        rating = div.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text
    except:
        rating = "N/A"

    # ✅ Store movie data
    movies[movie_name] = {
        "year": year,
        "length": length,
        "certificate": certificate,
        "rating": rating
    }

# ✅ Write to CSV (outside the loop)
with open('imdb_top_movies.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Movie Name", "Year", "Length", "Certificate", "Rating"])

    # Rows
    for name, info in movies.items():
        writer.writerow([name, info["year"], info["length"], info["certificate"], info["rating"]])

print("✅ CSV file saved as imdb_top_movies.csv")
