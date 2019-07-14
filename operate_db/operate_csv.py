import csv

with open('D:\\pythonSpider\\operate_db\\data.csv','w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['id','name','age'])
  writer.writerow(['1001','Alex','22'])
  writer.writerow(['1002','Alice','18'])