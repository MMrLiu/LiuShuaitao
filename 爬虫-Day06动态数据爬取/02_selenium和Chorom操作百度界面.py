
# 导入包
from selenium import webdriver
import time
# 设置当前谷歌浏览器不进行界面渲染
from selenium.webdriver.chrome.options import Options
# 创建一个配置
option = Options();
# option.headless = True # 无界面
# [1]调用谷歌驱动 - 带界面 - 效率低
driver = webdriver.Chrome(options=option)
# [2]请求一个网站
driver.get('https://www.i4.cn/')
# [3]获取网站数据源码
# data = driver.page_source
# print(data)
# file = open('baidu.html','wb',1)
# file.write(data);
# file.close
# [5]获取网页上的一些数据
# 5.1通过ID获取网页数据 - 遇到标签中包含文字的可以直接通过.text获取
t1 = driver.find_element_by_id('su')
print('[5.1--]',t1)
#获取返回对应中属性对应数据
print("[t1--]--value :",t1.get_attribute('value'))
# t2 = driver.find_element_by_class_name('mnav c-font-normal c-color-t').text
# print('[5.2]--',t2)
# [6]导入by模块
from selenium.webdriver.common.by import By
t3 = driver.find_element(By.ID,'su')
print('[6]--',t3.get_attribute('value'))
# 获取输入框
driver.find_element_by_id('kw').send_keys("千锋教育")
# 点击百度一下按钮
driver.find_element_by_id('su').click()
# 通过其他属性进行选择








time.sleep(5)
# [4]关闭浏览器
driver.quit()

