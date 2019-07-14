import re

content = 'Hello 1234567 World_This is a Regex Demo'
res = re.match('^He.*?(\d+).*Demo$',content)
print(res.group(1))