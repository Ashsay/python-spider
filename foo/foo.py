import requests
import json

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3860.5 Safari/537.36'
}

queryString = '/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A145AD835B1B4AF&cp=5D3B1BF4EAAF7E1&_signature=w.sGhRAZnsorIST4VHmdAsP7Bp'
data = requests.get('https://www.toutiao.com' + queryString, headers=headers)
res = json.loads(data.text)
print(json.dumps(res,indent=2))
