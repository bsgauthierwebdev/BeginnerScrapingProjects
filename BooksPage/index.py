# Practice project to scrape site http://books.toscrape.com/

# Import dependencies / libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_books():
    # Step 1: Set up Chrome options (headless mode means no browser window will open)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options = options)

    # Step 2: Define the target site
    try:
        url = 'https://books.toscrape.com'
        print('Loading page...')
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        page = 1

        while True:
            print(f'\n📄 Scraping page {page}...\n')

            wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'product_pod'))
            )

            books = driver.find_elements(By.CLASS_NAME, 'product_pod')

            print('\n📚 Books found...')

            for book in books:
                title = book.find_element(By.TAG_NAME, 'h3').find_element(By.TAG_NAME, 'a').get_attribute('title')
                price = book.find_element(By.CLASS_NAME, 'price_color').text
                availability = book.find_element(By.CLASS_NAME, 'availability').text.strip()
                rating_class = book.find_element(By.CLASS_NAME, 'star-rating').get_attribute('class')
                rating = rating_class.replace('star-rating', '').strip()

                print(f'Title: {title}')
                print(f'Price: {price}')
                print(f'Availability: {availability}')
                print(f'Rating: {rating} of Five Stars')
                print('-' * 60)

            try:
                next_button = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'li.next > a'))
                )
                next_button.click()
                page += 1
                time.sleep(1)
            except:
                print('🔚 No more pages to search')
                break

    except Exception as e:
         print("⚠️ An error occurred:", e)

    finally:
        driver.quit()

scrape_books()