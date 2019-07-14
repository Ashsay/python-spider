import requests
import re

class HandleLago(object):
  def __init__(self):
    self.lago_session = requests.session()
    self.header = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3833.0 Safari/537.36'
    }
    self.city_list = ''

  def handle_city(self):
    city_search = re.compile(r'zhaopin/">(.*?)</a>')
    city_url = "https://www.lagou.com/jobs/allCity.html"
    city_result = self.handle_request(method='GET',url=city_url)
    self.city_list = re.findall(city_search,city_result)
    self.lago_session.cookies.clear()

  def handle_city_job(self,city):
    first_request_url = ''%city
    first_response = self.handle_request(method='GET',url=first_request_url)
    print(first_response)
        
  def handle_request(self,method,url,data=None,info=None):
    if method == 'GET':
      response = self.lago_session.get(url=url,headers=self.header,verify=False)
    elif method == 'POST':
      response = self.lago_session.post(url=url,headers=self.header,verify=False)
    return response.text

if __name__ == '__main__':
  lago = HandleLago()
  lago.handle_city()
  for city in lago.city_list:
    lago.handle_city_job(city)
    break