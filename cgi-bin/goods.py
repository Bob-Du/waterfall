import cgi
import cgitb
import json

import pymongo

cgitb.enable()

print("Content-Type: text/html")
print()

fs = cgi.FieldStorage()  # 接收请求报文携带的数据

reqData = {}  # data字典存储整理后的请求信息
for key in fs:
    reqData[key] = fs[key].value

db = pymongo.MongoClient('db.bobdu.cc').waterfall
resData = list(db.goods.find({}, {'_id': 0}).skip(int(reqData['p'])*16).limit(16))

print(json.dumps(resData))
