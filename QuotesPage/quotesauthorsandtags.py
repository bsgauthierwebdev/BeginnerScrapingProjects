# Simple project to scrape https://quotes.toscrape.com/js/ and retrieve the Quote, Author & associated Tags

from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Optional, use webdriver-manater instead of manual chromedriver
from webdriver_manager.chrome import ChromeDriverManager