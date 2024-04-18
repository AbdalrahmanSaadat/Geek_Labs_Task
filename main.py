# importing Selenium and BeautifulSoup librarys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import time
import hashlib
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)

# hashing function
def hash_content(content, position):
    return hashlib.sha256(f'{content}_{position}'.encode('utf-8')).hexdigest()

# Set up the Selenium web driver
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
        
    # adding the Links
    driver.get('https://twitter.com/Mr_Derivatives')


    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

    # hashing symbols store
    unique_hashes = set()

    # count the appearence
    symbol_counts = {}
    
    position = 0


    while True:
        # parse the page using beautifulsoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # cashtag pattern
        tricker = re.compile(r'\$[A-Za-z]{3,4}')


        # Find all text matching the pattern
        symbols = soup.find_all(string=tricker)

        
        for symbol in symbols:
            symbol_string = symbol.strip('$').upper()
            position += 1
            symbol_hash = hash_content(symbol_string, position)
            
            if symbol_hash not in unique_hashes: 
                unique_hashes.add(symbol_hash)
                symbol_counts[symbol_string] = symbol_counts.get(symbol_string, 0) + 1

            
        
        # Scroll down function
        for _ in range(1): 
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            
        

except Exception as e:
    logging.error(f'an error occured: {e}')



finally: 

    # print the output
    for symbol, count in symbol_counts.items():
        print(f'{symbol}: {count}')
    # print(symbol)
    
    # quit the driver
    driver.close()
    driver.quit()
