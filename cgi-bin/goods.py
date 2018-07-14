import cgi
import cgitb
import json

import pymysql

cgitb.enable()

print("Content-Type: text/html")
print()

fs = cgi.FieldStorage()  # 接收请求报文携带的数据

reqData = {}  # data字典存储整理后的请求信息
for key in fs:
    reqData[key] = fs[key].value

connection = pymysql.connect(host='db.bobdu.cc', user='root', password='123456',
        db='waterfall', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

sql = 'select * from goods limit {}, 16'.format(int(reqData['p'])*16)
cursor.execute(sql)
resData = cursor.fetchall()

print(json.dumps(resData))