#coding=utf-8
import time
import random
import tesserocr
from PIL import Image

from seleniumFrame.ShowapiRequest import ShowapiRequest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
print(EC.title_contains("注册"))
wait = WebDriverWait(driver,10)

email = driver.find_element(By.ID,"register_email")
username = driver.find_element(By.ID,"register_nickname")
password = driver.find_element(By.ID,"register_password")

print('####select success#####')
print(email.get_attribute('placeholder'))

email.send_keys('1356988128@qq.com')
username.send_keys('Ashsay')
password.send_keys('mao19970315')
driver.save_screenshot('D:/pythonSpider/image.png')

code_element = driver.find_element(By.ID,"getcode_num")
l = code_element.location['x']
t = code_element.location['y']
right = code_element.size['width'] + l
height = code_element.size['height'] + t
im = Image.open('D:/pythonSpider/image.png')
img = im.crop((l,t,right,height))
img.save('D:/pythonSpider/image1.png')

image = Image.open('D:/pythonSpider/image1.png')
result = tesserocr.image_to_text(image)
print(result)

driver.close()