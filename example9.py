from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login")

wait = WebDriverWait(driver, 8)

Email = wait.until(
  EC.visibility_of_element_located((By.ID, "Email"))
)
Email.clear()
Email.send_keys("admin@yourstore.com")

driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

if(driver.title=="Dashboard / nopCommerce administration"):
  print("Login Success")
else:
  print("Login Failed")

driver.quit()



