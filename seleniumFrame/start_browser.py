#coding=utf-8
import time
import random
import tesserocr
from PIL import Image

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from seleniumFrame.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register')
print(EC.title_contains("注册"))
wait = WebDriverWait(driver,10)

email = driver.find_element(By.ID,"register_email")
username = driver.find_element(By.ID,"register_nickname")
password = driver.find_element(By.ID,"register_password")
captcha = driver.find_element(By.ID,"captcha_code")

print('####select success#####')
print(email.get_attribute('placeholder'))

email.send_keys('1356988128@qq.com')
username.send_keys('Ashsay')
password.send_keys('test123')
driver.save_screenshot('D:/pythonSpider/seleniumFrame/images/image.png')

code_element = driver.find_element(By.ID,"getcode_num")
l = code_element.location['x']
t = code_element.location['y']
right = code_element.size['width'] + l
height = code_element.size['height'] + t
im = Image.open('D:/pythonSpider/seleniumFrame/images/image.png')
img = im.crop((l,t,right,height))
img.save('D:/pythonSpider/seleniumFrame/images/image1.png')

r = ShowapiRequest("http://route.showapi.com/184-4","93925","5143fc3db0b5488b96a46724842767ce")
r.addFilePara("image","D:/pythonSpider/seleniumFrame/images/image1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "1")
res = r.post()
text = res.json()['showapi_res_body']['Result']

captcha.send_keys(text)

time.sleep(10)

driver.close()