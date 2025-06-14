import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.gsmarena.com.bd/meizu-note-22-pro/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

res = requests.get(url, headers=headers)

soup= bs(res.text,'html.parser')
# print(soup)
p_title= soup.find('h1')
print(p_title.text)