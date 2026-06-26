from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 10)

# Wait until username field is visible
username = wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
)
username.send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

wait.until(EC.title_contains("OrangeHRM"))

if driver.title == "OrangeHRM":
    print("Login test passed")
else:
    print("Login test failed")

driver.quit()