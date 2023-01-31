import datetime
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

# """Неявное ожидание"""
# driver.implicitly_wait(10)
# print("Start Test")
# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# visible_button.click()
# print("Finish Test")
"""Явное ожидание"""
print("Start Test")
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
visible_button.click()
print("Finish Test")


time.sleep(2)
driver.close()
