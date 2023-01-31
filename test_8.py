import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
# base_url = 'https://demoqa.com/checkbox'
# base_url = 'https://demoqa.com/radio-button'
# base_url = 'https://demoqa.com/buttons'
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

# """Select Check Box"""
# check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
# check_box.click()
# """Select Menu Check Box"""
# check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
# check_box.click()
# """Select Menu Radio Button"""
# radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
# radio_button.click()
# """Select Double and Right Click"""
# action = ActionChains(driver)
# double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
# action.double_click(double).perform()
#
# right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
# action.context_click(right_click).perform()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.clear() #Не все стирает, оставляет символы
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# new_date.send_keys("06/17/2022")
new_date.click()
time.sleep(2)
now_date = datetime.datetime.utcnow().strftime("%d")
print(now_date)
date = int(now_date) - 1
locator = f"//div[@aria-label='Choose Monday, January {date}th, 2023']"
print(locator)

date_17 = driver.find_element(By.XPATH, locator)
# date_17 = driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]")
date_17.click()

time.sleep(3)
driver.close()
