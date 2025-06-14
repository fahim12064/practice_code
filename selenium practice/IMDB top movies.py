from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top/")
sleep(5)
movies = driver.find_elements(By.CSS_SELECTOR, "h3.ipc-title__text")
for movie in movies:
    movie_name=movie.text
years=driver.find_elements(By.CSS_SELECTOR,'span.sc-4b408797-8')
# for year in years:
#     # movie_year=year.text
#     print(year.text)
rating=driver.find_elements(By.CSS_SELECTOR,"span.ipc-rating-star--rating")
for rate in rating:
    print(rate.text)