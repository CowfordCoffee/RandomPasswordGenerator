import requests
from bs4 import BeautifulSoup

def scrape_data(url, file_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = soup.find_all('div', class_='item')

    with open(file_path, 'w') as file:
        for item in data:
            file.write(item.text + '\n')
