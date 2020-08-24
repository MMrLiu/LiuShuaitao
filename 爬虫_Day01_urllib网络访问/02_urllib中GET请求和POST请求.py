
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# [1]导入包
import urllib.request,urllib.parse
# [2]Get请求
ce_url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&'
keyword = input("请输入您要百度的内容:\n")
# wd=爱思助手
# urlencode函数 可以把字典对象转换为get请求的参数
dic_word={'wd':keyword}
code = urllib.parse.urlencode(dic_word)
# 网址拼接
bd_url = ce_url+code
print(bd_url)
# 把网址进行中文转换
print(urllib.request.unquote(bd_url))
# 百分号编码
ce_url_01 = 'https://www.baidu.com/s?wd=扣丁学堂'
print(ce_url_01)
# 也可以理解为加密
print(urllib.request.quote(ce_url_01)) # 用在网址恶意木马软件访问
resp = urllib.request.urlopen(bd_url)
print("当前Get请求的地址：",resp.url)


# [2]POST请求
# 2.1测试网址
post_url = 'http://httpbin.org/post'
# 2.2定义一下表单参数
data_dic = {'username':'123','password':'123456'}
# 2.3把字典形式转换
data_str = urllib.parse.urlencode(data_dic)
# 2.4一般情况下：post请求都是使用二进制参数
data_code = bytes(data_str,encoding='utf-8');
resp = urllib.request.urlopen(post_url,data=data_code)
# 输出请求结果
print(resp.read().decode('utf-8'))
print("当前的请求网址：",resp.url)