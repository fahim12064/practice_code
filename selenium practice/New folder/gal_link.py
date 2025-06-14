from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import json

driver = webdriver.Chrome()
driver.get("https://www.erome.com/search?q=thick+muslim")
sleep(8)

pics=driver.find_elements(By.CSS_SELECTOR,"div.grid-item a")
data=[]

for pic in pics:
    title=pic.get_attribute("title") or "No Title"
    url=pic.get_attribute("href")
    data.append({"title": title, "url": url})  # ✅ এই লাইন ছিল না
    print(f'{title}={url}')
with open("gallery_links.json","w",encoding='utf-8')as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

driver.quit()