# import time
# import pymysql
# from selenium import webdriver
# from lxml import etree
# from selenium.webdriver.common.by import By
#
# conn = pymysql.connect(user='root', host='127.0.0.1', password='824921', port=3306, db='spider')
# cursor = conn.cursor()
#
#
# def insert_sql(data):
#     cursor.execute(f'''insert into epidemic values {data} ''')
#     conn.commit()
#
#
# browser = webdriver.Chrome()
# url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/'
# browser.get(url=url)
#
# browser.find_element(By.XPATH, '//*[@id="ptab-0"]/div[2]/div[2]/div[3]/div/span').click()
# time.sleep(2)
# tree = etree.HTML(browser.page_source)
# tup = ()
# print("开始写入数据库*****")
# for i in tree.xpath('//*[@id="ptab-0"]/div[2]/div[2]/div[2]/a'):
#     place = i.xpath('./div/div[1]/div/span[1]/text()')[0]
#     add_num = i.xpath('./div/div[2]/text()')[0]
#     now_num = i.xpath('./div/div[3]/text()')[0]
#     tup = (place, add_num, now_num)
#     insert_sql(tup)
# print("写入数据库结束*****")
# cursor.close()
# conn.close()
