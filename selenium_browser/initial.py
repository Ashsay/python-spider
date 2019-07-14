from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

try:
  browser.get('https://www.baidu.com')
  input_keys = browser.find_element(By.ID,'kw')
  input_keys.send_keys('python')
  input_keys.send_keys(Keys.ENTER)
  wait.until(EC.presence_of_element_located((By.ID,'content_left')))
  print(browser.current_url)
  print(browser.get_cookies())
  print(browser.page_source)
finally:
  browser.close()