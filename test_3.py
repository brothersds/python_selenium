import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
# time.sleep(1)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(1)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(1)
# user_name.send_keys("er")
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print("Input Password")
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print("Click Login Button")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter.click()
print("Click Filter")
time.sleep(2)
# filter.send_keys(Keys.PAGE_DOWN)
filter.send_keys(Keys.DOWN)
time.sleep(1)
filter.send_keys(Keys.RETURN)
time.sleep(3)
