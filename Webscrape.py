import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request to the URL of the webpage you want to scrape
url = "https://www.gmail.com"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    print("Title of the webpage retrieved:", title)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
