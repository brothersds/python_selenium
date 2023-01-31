import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)

round_slider = driver.find_element(By.XPATH, "//input[@id='id1']")
action.click_and_hold(round_slider).move_by_offset(150, 0).release().perform()

print("Round +")


time.sleep(1)
driver.close()
