import json
import requests
from requests.exceptions import RequestException
import re
import time

def get_one_page(url):
  try:
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3833.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers,verify=False)
    print(response)
    if response.status_code == 200:
      return response.text
    return None
  except RequestException:
    return None

def parse_one_page(html):
  pattern = re.compile(
    r'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
    re.S
  )
  items = re.findall(pattern,html)
  arr = []
  for i in items:
    yield {
      'index':i[0],
      'image':i[1],
      'title':i[2].strip(),
      'actor':i[3].strip()[3:] if len(i[3])>3 else '',
      'time':i[4].strip()[5:] if len(i[4])>5 else '',
      'score':i[5].strip()+i[6].strip()
    }

def write_to_file(content):
  with open('result.txt','a',encoding='utf-8') as f:
    f.write(json.dumps(content,ensure_ascii=False)+'\n')

if __name__ == '__main__':
  html = get_one_page('https://maoyan.com/board')
  for i in parse_one_page(html):
    print(i)