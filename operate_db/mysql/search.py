import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spider')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
  cursor.execute(sql)
  row = cursor.fetchone()
  while row:
    print(row)
    row = cursor.fetchone()
except:
  print('Error')