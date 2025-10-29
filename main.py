import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to fetch the webpage
url = "https://example.com"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract the required data (e.g., the title of the page)
title = soup.find('title').get_text()
print("Page Title:", title)