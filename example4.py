from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://google.com")
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search.send_keys("Python Selenium")
search.send_keys(Keys.ENTER)
input("Press Enter to close...")
driver.quit()

