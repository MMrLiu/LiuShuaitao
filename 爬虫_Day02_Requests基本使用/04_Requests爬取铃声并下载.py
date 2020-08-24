'''整合练习'''
# [1]导入包
import re
import requests
import random
# [2]目标网址
as_url = 'https://www.i4.cn/ring_3_0_1.html'
# [3]配置文件
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
# [4]训练代理IP(本案例无需使用代理IP)在下载的时候使用代理IP
IP_list=[{'htts://':'59.33.54.91:9999'},
         {'htts://':'183.166.97.51:9999'},
         {'htts://':'183.166.96.136:9999'},
         {'htts://':'183.166.96.90:9999'},
         {'htts://':'183.166.171.176:8888'}]
# [5]本身的网络数据只请求一次所以只使用默认IP
resq_data = requests.get(url=as_url,headers= header,timeout=10)
# [6]检查一下网络是否请求成功
if resq_data.status_code == requests.codes.ok:
    # [7]读取数据
    data = resq_data.text
    # [8]数据的本地存储
    file_as = open('爱思助手.html','w',encoding='utf-8')
    file_as.write(data)
    file_as.close()
    # [8]创建正则表达式模板
    r = r'<div class="list ring_list">\s*<div class="img">\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*'
    pat = re.compile(r)
    # 查询匹配40首音乐
    div_list = re.findall(pat,data)
    # [9]通过遍历for循环的形式进行查询每一首音乐
    for i in range(0,len(div_list)):
        print("第%d首音乐-----------"%i)
        item_div = div_list[i]
        print(item_div)
        # 通过正则表达式匹配音乐名称
        name_div = re.findall(re.compile(r'<div class="title" title=".*'),item_div)
        # print("音乐名称：",name_div)
        name_mp3 = re.findall(re.compile(r'>(.*)<'),name_div[0])[0]
        print("音乐名称：", name_mp3)
        # 音乐地址
        mp3_url = re.findall(re.compile(r'[a-zA-z]+://[^\s]*.mp3'),item_div)[0]
        print("音乐地址：",mp3_url)
        # 音乐下载：使用代理IP下载
        # 随机选取代理IP
        item_ip = IP_list[random.randint(0,len(IP_list)-1)]
        # 使用代理IP下载
        print("使用带代理IP:",item_ip)
        # 开始下载
        # res_mp3 = requests.get(url=mp3_url,proxies=item_ip,headers=header)
        res_mp3 = requests.get(url=mp3_url, headers=header)
        mp3_data = res_mp3.content
        # 把数据存储成音乐
        print("正在下载第%d首音乐：%s"%(i,name_mp3))
        item_mp3 = open("mp3\%s.mp3"%name_mp3,'wb',1)
        item_mp3.write(mp3_data)
        item_mp3.close()



        pass


    print(div_list)
    pass
else:
    print('网络异常')
    pass



