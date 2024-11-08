from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time


def search(prompt:str):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://google.com")
    
    elem = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    elem.send_keys(prompt + Keys.ENTER)

    time.sleep(1)

    driver.find_elements(By)   

    final_links = []
    links = driver.find_elements(By.CSS_SELECTOR, 'h3')
    for link in links:
        final_links.append(link.find_element(By.XPATH, '..').get_attribute('href'))

    return final_links
    