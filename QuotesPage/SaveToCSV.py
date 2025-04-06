# Web scraper to pull data from site https://quotes.toscrape.com/js/ and save to a CSV file

import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_quotes_to_csv():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size-1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options = options)

    all_quotes = []

    try:
        url = 'https://quotes.toscrape.com/js/'
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        page = 1
        while True:
            print(f'\n📄 Scraping page {page}...\n')
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote')))
            quotes = driver.find_elements(By.CLASS_NAME, 'quote')

            for quote in quotes:
                text = quote.find_element(By.CLASS_NAME, 'text').text
                author = quote.find_element(By.CLASS_NAME, 'author').text
                tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, 'tag')]

                all_quotes.append({
                    'text': text,
                    'author': author,
                    'tags': ', '.join(tags)
                })

            try:
                next_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.next > a')))
                next_button.click()
                page += 1
                time.sleep(1)
            except:
                print("🔚 No more pages to scrape.")
                break

    except Exception as e:
        print("⚠️ An error occurred:", e)

    finally:
        driver.quit()

    # ✅ Save to CSV
    with open('quotes.csv', 'w', newline = '', encoding = 'utf-8') as f:
        writer = csv.DictWriter(f, fieldnames = ['text', 'author', 'tags'])
        writer.writeheader()
        writer.writerows(all_quotes)
        print('💾 Quotes saved to "quotes.csv"')

scrape_quotes_to_csv()