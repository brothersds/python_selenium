import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()

# """Select Check Box"""
# check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
# check_box.click()
"""Select Menu Check Box"""
check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
check_box.click()

time.sleep(2)
driver.close()
