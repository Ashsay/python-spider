import re

html = '''<div>
  <h2>classic music</h2>
  <dl>
    <dd class="list_item">1</dd>
    <dd class="list_item">2</dd>
    <dd class="list_item">3</dd>
  </dl>
</div>'''

results = re.findall(r'<dd.*?class="(.*?)">(.*?)</dd>',html,re.S)
for item in range(0,len(results)):
  print(results[item])