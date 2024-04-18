# importing Selenium and BeautifulSoup librarys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time

# Set up the Selenium web driver
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

# adding the Links
driver.get('https://twitter.com/Mr_Derivatives')


time.sleep(5)

# Scroll down function
for _ in range(5): 
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)  


# parse the page using beautifulsoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# cashtag pattern
tricker = re.compile(r'\$[A-Za-z]{3,4}')

# Find all text matching the pattern
symbols = soup.find_all(string=tricker)

# print the output
for symbol in symbols:
    print(symbol)

# quit the driver
driver.quit()
