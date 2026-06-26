from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
message = driver.find_element(By.ID, "flash")
print(message.text.replace("×", "").strip())
time.sleep(5)
driver.quit()