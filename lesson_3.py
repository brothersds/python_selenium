from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/python_selenium/chromedriver')
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
