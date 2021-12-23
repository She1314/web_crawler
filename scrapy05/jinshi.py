from selenium import webdriver
from bs4 import BeautifulSoup
import time, re, os

url = 'https://www.jin10.com/'
driver = webdriver.Edge()  # 模拟打开浏览器
driver.get(url)
# 解析网页
soup = BeautifulSoup(driver.page_source, 'lxml')
# data = driver.find_element_by_class_name('jin-flash_item J_flash_item important ')
# print(soup)
info = str(soup.select('.jin-flash_list')[0])  # 转换为字符串格式，用正则表达式进行抽取


# print(info)

def get_info():
    reg = re.compile(r'<div class="jin-flash_item J_flash_item important " data-id="(.*?)".*?<p class=".*?">(.*?)</p>',
                     re.S)
    datas = re.findall(reg, info)
    # print(datas)
    return datas


def save_info(datas):
    if os.path.exists("4") == True:
        print('该文件已存在')
    else:
        os.mkdir("4")
    a = 1
    for data in datas:
        x = time.strftime('%Y-%m-%d %H:%M:%S')  # 筛选时间段,默认当前时刻
        y = time.strftime('%Y-%m-%d %H:%M:%S')
        if x < data[0] < y:
            data = data[1]  # 取事件
            # print(data)
            data = data.replace('<b>', '').replace('</b>', '').replace('<br/>', '')
            with open(r"4\info.txt", 'a', encoding='utf-8') as f:
                f.write(data + '\n')
                print('正在抓取第{}条important数据'.format(a))
                a += 1
    print('抓取结束！')


datas = get_info()
save_info(datas)
# time.sleep(1)
driver.close()
