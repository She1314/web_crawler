# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
response = session.get(url=url)

print(response.html)
for div in response.html.xpath('//div[@class="j_joblist"]/div'):
    jop = div.xpath('./a/p[1]/span[1]/text()')
    salary = div.xpath('./a/p[2]/span[1]/text()')
    place = div.xpath('./a/p[2]/span[2]/text()')
    print(div)
