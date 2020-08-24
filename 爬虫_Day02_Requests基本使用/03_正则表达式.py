
# [1]导入正则表达式包
import re
# [2]Python正则表达式常规使用
data = ''
r = r''
# 创建一个模板
pat = re.compile(r)
# 进行数据匹配- 返回值 - 数组形式
data_list= re.findall(pat,data)
# =============================
# [1]. 表示任意字符,如果说指定了DOTALL的标识,就表示包括新行在内的所有字符。
# .只能表示一个任意字符 .*表示多个任意字符匹配
res_01 = re.findall(re.compile(r'a.*c'),'cadfsfdsfdsc')
print('[1]====:',res_01)
# [2]^表示字符串开头。
res_01 = re.findall(re.compile(r'^a.c'),'cabc')
print('[2]====:',res_01)
# [3]'*"表示匹配前一个字符重复0次到无限次,
res_01 = re.findall(re.compile(r'ab*c'),'cac')
print('[3]====:',res_01)
# [4]'+'表示匹配前一个字符重复1次到无限次,
res_01 = re.findall(re.compile(r'ab+c'),'cabbbbbc')
print('[4]====:',res_01)
# [5]?'表示匹配前一个字符重复0次到1次
res_01 = re.findall(re.compile(r'ab?c'),'cabc')
print('[5]====:',res_01)
# [6]匹配前一个字符m次
res_01 = re.findall(re.compile(r'ab{2}c'),'cabbc')
print('[6]====:',res_01)
# [7]匹配前一个字符m到n次
res_01 = re.findall(re.compile(r'ab{2,8}c'),'cabbbbc')
print('[7]====:',res_01)
# [8]匹配前一个字符m到n次{m,n}?失效
# res_01 = re.findall(re.compile(r'ab{2,8}c'),'cabbcabbbc')
# print('[7]====:',res_01)
# [9]对特殊字符进行转义,或者是指定特殊序列 \
res_01 = re.findall(re.compile(r'c\.b'),'cabbbbc.b')
print('[9]====:',res_01)
# [10]()被括起来的表达式作为一个分组. findall在有组的情况下只显示组的内容
res_01 = re.findall(re.compile(r'c(.*)b'),'abbbbc12345b')
print('[9]====:',res_01)
#
# <div class="title" >安心亚 - 来追我男友吧  </div>
res_01 = re.findall(re.compile(r'>(.*)<'),'da<div class="title" >安心亚 - 来追我男友吧  </div>')
print('[0]====:',res_01)






