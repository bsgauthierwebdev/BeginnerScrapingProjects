# Step 1: Set up Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os


# Test webdriver to make sure it's working
# driver = webdriver.Chrome()  # It will look for chromedriver in the current folder
# driver.get("https://www.google.com")
# print("Opened Google!")
# driver.quit()

# Set up the chromedriver link

# Correct full path to chromedriver.exe
chromedriver_path = r"C:\Users\Brent\Desktop\Web Projects\PythonProjects\BeginnerScrapingProjects\RedditScraper\chromedriver.exe"

# Step 2: Configure Selenium Options (Headless Mode optional)
options = Options()
options.add_argument('--start-maximized') # Optional: --headless for silent mode

# Create the WebDriver with the Service object
service = Service(executable_path = chromedriver_path)
driver = webdriver.Chrome(service = service, options = options)

# Step 3: Open Reddit and wait for posts to load
url = 'https://www.reddit.com/r/Python/'
driver.get(url)

# Reddit might show a popup or delay content
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'shreddit-post')))

# Wait for JS content to finish rendering
time.sleep(3)

# Step 4: Grab page source and use BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Step 5: Extract post info
posts = soup.find_all('shreddit-post')
for post in posts:
    try:
        title_tag = post.find(attrs = {'slot': 'title'})
        title = title_tag.text.strip() if title_tag else 'No title found'

        link_tag = post.find('a', href = True)
        link = 'https://www.reddit.com' + link_tag['href'] if link_tag else 'No link found'

        upvote_tag = post.find('faceplate-number')
        upvotes = upvote_tab.text.strip() if upvote_tag else '0'

        print(f'Title: {title}')
        print(f'Link: {link}')
        print(f'Upvotes: {upvotes}')
        print('-' * 40)

    except Exception as e:
        print('Error parsing post:', e)

# Step 6: Close the driver
driver.quit()