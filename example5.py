from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
heading = driver.find_element(By.TAG_NAME, "h2")
print(heading.text)
button = driver.find_element(By.TAG_NAME, "button")
print(button.text)
time.sleep(5)
driver.quit()