import random

for i in range(10):
  user_email = ''.join(random.sample('1234567890abcdefghijklmn',10))+'@163.com'
  print(user_email)