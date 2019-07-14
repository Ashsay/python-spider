#codding:utf-8
import urllib.request

response = urllib.request.urlopen('https://www.baidu.com')
print(response.read().decode('utf-8'))