import scrapy
from selenium import webdriver

'''
validateId: 49db294248b44af4a76a515b9aa36025
validateData: %7B%22type%22%3A20%2C%22geetest_challenge%22%3A%22440f532d56eb919bac1364c444123a8598%22%2C%22geetest_validate%22%3A%22885fb0a686bfec5be548299030128c3a%22%2C%22geetest_seccode%22%3A%22885fb0a686bfec5be548299030128c3a%7Cjordan%22%7D
passport: 121212121
password: 12313131
rememberMe: true
sessionId: 51a7b085s0bea440258f085126bd49f4d989
thirdVerifyId: a41c400d-32f7-4398-a852-7138c7244863
verifyType: 1
time: 1640870071889
refer: 121126445
redirectURL: %2F%2Fi.zhaopin.com%2Fblank%3Fhttps%3A%2F%2Fwww.zhaopin.com%2F%3F
appID: 9f69dd17cf834693b04e06dd5e9b5728
refer_base: 1211
source: 
'''


class WymusicSpider(scrapy.Spider):
    name = 'wymusic'
    # allowed_domains = ['https://music.163.com/']
    start_urls = ['https://music.163.com/#/song?id=1367452194', 'https://music.163.com/#/song?id=186345',
                  'https://music.163.com/#/song?id=28059417', 'https://music.163.com/#/song?id=191254']

    def __init__(self):
        self.bro = webdriver.Chrome()

    def parse(self, response):
        for url in self.start_urls:
            for div in response.xpath('//div[@class="cmmts j-flag"]/div'):
                content = div.xpath('./div/div[2]//text()').extract()
                print(content)
            yield scrapy.Request(url=url, callback=self.parse)
