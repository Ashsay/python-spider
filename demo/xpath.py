from lxml import etree

html = etree.parse('D:\\py-django\\resource\\html\\xpath.html',etree.HTMLParser())
result = html.xpath('//li[@class="item0"]//a//text()')[0]
print(result)