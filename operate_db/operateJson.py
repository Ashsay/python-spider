import json

str = '''
[{
  "name":"Alex",
  "age":22,
  "sex":"man"
}]
'''

data = json.loads(str)
print(data[0].get('name'))


dic = [{
  "name":"Alex",
  "age":22,
  "sex":"man"
}]
with open('D:\\pythonSpider\\operate_db\\data.json','w') as files:
  files.write(json.dumps(dic,indent=2))