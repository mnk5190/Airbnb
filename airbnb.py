import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait

# Synchronization: When we write selenium code, every statement will execute top to bottom. Implicit Waits & Explicit Waits.
driver = webdriver.Chrome(executable_path = "C:/Users/khan/Downloads/chromedriver_win32/chromedriver.exe")

# Wait some time here
driver.implicitly_wait(5) # seconds

# Maximize the window()
driver.maximize_window()
driver.get("https://www.airbnb.com")
# fill out the city
driver.find_element_by_id("Koan-magic-carpet-koan-search-bar__input").send_keys("toronto")
driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/ul[1]/li[1]/div[2]/div[1]/span[1]").click()
driver.implicitly_wait(5)

# fill out the check-in date

driver.find_element_by_xpath("//input[@id='checkin_input']").click()
driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'4')]").click()

# fill out the Check-out date

driver.find_element_by_xpath("//input[@id='checkout_input']").click()
driver.find_element_by_xpath("//div[@class='_1lds9wb']//td[@class='_1wh4xpp1'][contains(text(),'20')]").click()

#Guest

driver.find_element_by_xpath("//button[@class='_7ykwo4']").click()
driver.find_element_by_xpath("//div[@class='_9cfq872']//div//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1]").click()
driver.find_element_by_xpath("//button[@class='_1dv8bs9v']").click()
driver.find_element_by_xpath("//span[contains(text(),'Search')]").click()