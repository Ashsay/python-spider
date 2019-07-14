#codding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome Dev\Application\chromedriver.exe')
wait = WebDriverWait(browser,10)

browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
# cookies = [] 通过注入cookie登入淘宝
cookies = []
for item in cookies:
  browser.add_cookie(item)
time.sleep(2)
link_tianmao = browser.find_element(By.LINK_TEXT,'天猫超市')
link_tianmao.click()
browser.switch_to_window(browser.window_handles[2])
mq = browser.find_element(By.ID,'mq')
mq.send_keys('乐事薯片')
mq.send_keys(Keys.ENTER)
time.sleep(5)



