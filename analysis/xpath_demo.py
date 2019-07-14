from lxml import etree

html = etree.parse('D:\\pythonspider\\analysis\\xpath.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
attr = html.xpath('//li[contains(@class,"list") and @name="zero"]/a/text()')
print(result,attr)