import requests
from bs4 import BeautifulSoup

URL = "https://www.jbhifi.com.au/collections/computers-tablets/laptops"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer") # div = ais-hits--item
print(results)