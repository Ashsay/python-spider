import pymysql

table = 'students'
condition = 'age > 20'

db = pymysql.connect(local='localhost',user='root',password='root',port=3306,db='spider')
cursor = db.cursor()
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
  cursor.execute(sql)
  db.commit()
except:
  db.rollback()

db.close()