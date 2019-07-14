from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'

class CrackGeetest():
  def __init__(self):
    self.url = 'https://account.geetest.com/login'
    self.browser = webdriver.Chrome()
    self.wait = WebDriverWait(self.browser,20)
    self.email = EMAIL
    self.password = PASSWORD

  def get_geetest_button(self):
    '''
    获取初始验证按钮
    :return:按钮对象
    '''
    self.browser.get(self.url)
    usr = self.browser.find_element()
    pwd = self.browser.find_element()
    usr.send_keys(EMAIL)
    pwd.send_keys(PASSWORD)
    button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
    return button

if __name__ == '__main__':
    geetest = CrackGeetest()
    button = geetest.get_geetest_button()
    button.click()