from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_quotes():
    # Step 1: Set up Chrome options (headless mode means no browser window will open)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Step 2: Create the Selenium WebDriver (this is the browser robot)
    driver = webdriver.Chrome(options=options)

    try:
        # Step 3: Go to the quotes website
        url = 'https://quotes.toscrape.com/'
        print('Loading page...')
        driver.get(url)

        # Step 4: Wait for the quotes element to load (based on their class name)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote'))
        )

        # Step 5: Extract the quotes
        quotes = driver.find_elements(By.CLASS_NAME, 'quote')

        # Step 6: Print the quotes
        print("\n📝 Quotes found:")
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, 'text').text
            author = quote.find_element(By.CLASS_NAME, 'author').text
            tag_elements = quote.find_elements(By.CLASS_NAME, 'tag')
            tags = [tag.text for tag in tag_elements]
            print(f'✅ {text}')
            print(f'- {author}')
            print(f'Tags: {", ".join(tags)}')
            print('-' * 60)

    except Exception as e:
        print("⚠️ An error occurred:", e)
    
    finally:
        # Step 7: Close the browser
        driver.quit()

scrape_quotes()