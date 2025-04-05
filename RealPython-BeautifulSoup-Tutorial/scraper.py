# This is a tutorial from Real Python
# https://realpython.com/beautiful-soup-web-scraper-python/#step-3-parse-html-code-with-beautiful-soup

import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'ResultsContainer')

# print(results.text.strip())

python_jobs = results.find_all(
    'h2', string = lambda text: 'python' in text.lower()
)

# print(python_jobs)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# print(python_job_cards)

for job_card in python_job_cards:
    title = job_card.find('h2', class_ = 'title')
    company = job_card.find('h3', class_ = 'company')
    location = job_card.find('p', class_ = 'location')
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    link_url = job_card.find_all('a')[1]['href']
    print(f'Apply here: {link_url}\n')
    print('-' * 20)