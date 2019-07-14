from urllib.parse import urlencode
import requests
baseUrl = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
  'Host':'m.weibo.cn',
  'Referer':'https://m.weibo.cn/u/2830678484',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3824.6 Safari/537.36',
  'X-Requested-With':'XMLHttpRequest'
}

def get_page(page):
  params = {
    'type':'uid',
    'value':'2830678474',
    'containerid':'1076032830648474',
    'page':'page'
  }
  url = baseUrl + urlencode(params)
  try:
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
      return response.json()
  except requests.ConnectionError as e:
    print('error',e.args)