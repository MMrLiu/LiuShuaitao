
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 【1】导入包
import urllib.request,urllib.parse
import re
# 【2】目标网址
as_url = 'https://www.i4.cn/wper_1_0_0_1.html'
# 【3】配置网络请求信息头
"""
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
"""
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
          'Host':'www.i4.cn'}
req = urllib.request.Request(url=as_url,headers=header,method='GET',data=None)
# 【4】网络请求-并读取
resq = urllib.request.urlopen(req);
if resq.code == 200:
    data = resq.read();
    # 【5】本地数据保存
    as_file = open('爱思助手-手机壁纸.html', 'wb', 1)
    as_file.write(data)
    as_file.close()
    # 【6】通过正则表达式进行匹配数据 - 导入正则表达式包
    r = r'[a-zA-z]+://[^\s]*.jpg';
    # 只要大图
    r = r'https://d-paper.i4.cn/max/[^\s]*.jpg';
    # 【7】创建正则表达式模板
    pat = re.compile(r);
    # 【8】进行数据匹配str(data)
    img_list = re.findall(pat,data.decode('utf-8'))
    print(len(img_list),img_list)
    # 【9】下载图片
    for i in range(0,len(img_list)):
        print("正在下载第%d张图片----"%i)
        item_url = img_list[i] #每张图片的地址
        print("图片地址：",item_url)
        # 下载文件：第一个参数：文件的地址 第二个参数：文件另存为
        urllib.request.urlretrieve(item_url,"img/第%d张.jpg"%i)

        pass

    pass
else:
    print("网络异常")
    pass

# ====================
"""
作业：
1.复习urllib网络请求的使用
2.复习爱思助手壁纸爬取
3.爬取爱思助手铃声 - 保存到本地（把对应数据保持到数据库中）

"""

