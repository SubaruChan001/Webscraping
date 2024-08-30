import requests
from bs4 import BeautifulSoup

url = "https://www.gmail.com"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string
    print("Title of the webpage retrieved:", title)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
