
# [1]下载第三方库
import pymongo
# [2]链接MongoDB数据库
# client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
client = pymongo.MongoClient(host='localhost',port=27017)
# [3]创建数据库 - 和 选择使用数据库一致
# 如果选择的数据库不存在就会创建该数据库 - 不会直接在数据库展示
# 在创建集合的时候 - 相当于关系型数据库中的表
db = client.test_01
# [4]创建集合 或 选择集合
collection = db.c1
# [5]给集合中插入数据
data_01 = {"username":'张良','age':10,"add":'帝都'}
data_02 = {"username":'夏侯惇','age':18,"add":'帝都+1'}
"""
Use insert_one or insert_many
注意：insert已经被舍弃 
insert函数- 插入数据-返回被插入数据的ID 
"""
# result = collection.insert_one(data_01);
# [6]输出数据
# 5f3e7bc2f1d53f5bbf7374d1
# 5f3e7bc2f1d53f5bbf7374d1
# print("[6]--",result)
# 5f3e7cd79042b443791ae252
# print("[6]查看ID--",result.inserted_id)
"""
MongoDB 会对每一条数据自动生成一个：ObjectId类型的_id值作为当前这条数据的唯一标识
"""
# [7]插入多条数据
result = collection.insert_many([data_01,data_02]);
print('[7]--',result)
print('[7]插入多条返回值：--',result)
# [8]删除值
"""
Use delete_one or delete_many 
"""
# result = collection.remove({'add':'帝都+1'})
print('[8]--',result) # {'n': 7, 'ok': 1.0} 返回值- 删除7条 表示执行成功
# result = collection.delete_one({'age':18})
# 数据 - 先进先出形式
# print('[8]delete_one--',result)
# [9]-修改数据
# 值修改一条
# result = collection.update({"username":'张良','age':10,"add":'帝都'},{"username":'狄仁杰','age':10,"add":'帝都'})
# print('[9]--',result)
"""
replace_one, update_one or update_many
"""
result = collection.replace_one({"username":'张良','age':10,"add":'帝都'},{"username":'甄姬','age':30,"add":'帝都'})
print('[9]replace_one--',result)
# 替换多条
# result = collection.replace_many({"username":'张良','age':18,"add":'帝都'},{"username":'甄姬1','age':302,"add":'帝都'})
# print('[9]replace_many--',result)
# [10]find_one
result = collection.find({'age':{'$lt':18}})
print('[10]---',result)
# Cursor 游标 理解为集合的形式
for item_data in result:
    print('--',item_data)
    pass
# [11]
result = collection.find({'username':{'$regex':'狄.杰'}})
print('[11]---',result)
# Cursor 游标 理解为集合的形式
for item_data in result:
    print('--',item_data)
    pass

"""
find_one_and_delete() 查找一个并删除 
find_one_and_update()

"""




