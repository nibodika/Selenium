from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Terraform")
search.send_keys(Keys.ENTER)
time.sleep(3)
driver.back()
search = driver.find_element(By.NAME, "q")
search.send_keys("Python Selenium")
search.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()