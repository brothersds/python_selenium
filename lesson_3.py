import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
#driver = webdriver.Firefox(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium')
s = Service('/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
#user_name = driver.find_element(By.ID, "user-name")    # ID
# user_name = driver.find_element(By.NAME, "user-name")   # NAME
# user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")   # Full XPATH
# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")   # ID XPATH
user_name = driver.find_element(By.XPATH, "//input[@data-test='username']")   # data-test XPATH
user_name.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "#password")    # CSS_SELECTOR
password.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()
time.sleep(3)
driver.close()
