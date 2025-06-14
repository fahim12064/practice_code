from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
sleep(10)
elements = driver.find_elements(By.CSS_SELECTOR,"a#video-title")
with open("youtube_trending_video.csv","w",newline="",encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(["Title","URL"])
        for ele in elements:
                name=ele.text
                link= ele.get_attribute("href")
                writer.writerow([name,link])
driver.quit()
