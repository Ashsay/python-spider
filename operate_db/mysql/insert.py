import pymysql

data = {
  'name':'Ashsay',
  'age':22,
  'id':'00001'
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

db = pymysql.connect(host='localhost',user='root',password='root',db='spider')
cursor = db.cursor()
sql = 'INSERT INTO {table} ({keys}) VALUES ({values}) NO DUPLICATE KEY UPDATE'.format(table=table, keys=keys,values=values)
try:
  if cursor.execute(sql,tuple(data.values())):
    db.commit()
    print('success')
except:
  db.rollback()
db.close()