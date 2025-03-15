from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# Test Chrome
chrome_service = ChromeService()
chrome_driver = webdriver.Chrome(service=chrome_service)
chrome_driver.get("https://www.google.com")
print(chrome_driver.title)
chrome_driver.quit()

# Test Firefox
service = FirefoxService()
driver = webdriver.Firefox(service=service)
driver.get("https://www.google.com")
print(driver.title)
driver.quit()