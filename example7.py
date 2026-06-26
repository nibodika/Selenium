from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print("Checkbox 1:", checkboxes[0].is_selected())
print("Checkbox 2:", checkboxes[1].is_selected())
if not checkboxes[0].is_selected():
         checkboxes[0].click()
print("Checkbox 1 after click:", checkboxes[0].is_selected())
time.sleep(5)
driver.quit()