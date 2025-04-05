from selenium import webdriver
from selenium.webdriver.chrome.service import Service # Import the Service class
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Step 1: Set up Chrome options (optional for headless browsing)
options = Options()
options.headless = False # Set to True if you want to run the browser without a UI

# Step 2: Specify the path to ChromeDriver using Service
service = Service(r"C:\Users\Brent\Desktop\Web Projects\PythonProjects\BeginnerScrapingProjects\webscraping-tutorial\drivers\chromedriver.exe") 

# Step 3: Initialize the WebDriver with the Service object and options
driver = webdriver.Chrome(service=service, options=options)

# Step 4: Open a website
driver.get('http://quotes.toscrape.com/js/')

# Step 5: Scrape quotes from the page
quotes = driver.find_elements(By.CLASS_NAME, 'text')

for quote in quotes:
    print(quote.text)

# Step 6: Close the browser
driver.quit()