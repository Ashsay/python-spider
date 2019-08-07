#coding=utf-8
from PIL import Image
import tesserocr
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from seleniumFrame.ShowapiRequest import ShowapiRequest
image = Image.open('D:/pythonSpider/seleniumFrame/images/image1.png')

r = ShowapiRequest("http://route.showapi.com/184-4","93925","5143fc3db0b5488b96a46724842767ce")
r.addFilePara("image","D:/pythonSpider/seleniumFrame/images/image1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "1")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(res.text) # 返回信息

result1 = tesserocr.image_to_text(image)
print(result1)

