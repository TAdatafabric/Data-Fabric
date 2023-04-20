import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.example.com'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = []

for row in soup.find_all('tr'):
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

df = pd.DataFrame(data, columns=['Column 1', 'Column 2', 'Column 3'])

df.to_csv('data.csv', index=False)
