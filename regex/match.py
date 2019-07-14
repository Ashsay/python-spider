import re

content = 'Hello 123 4567 World_This is a Regex Demo'
res = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(res)
print(res.group())