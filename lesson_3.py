import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

#driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
#driver = webdriver.Firefox(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium')
s = Service('/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(10)
driver.close()
