import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class DouyuSpider(scrapy.Spider):
    name = "longzhu"
    webFunc = WebFunc()
    start_urls = [
        "http://longzhu.com/channels/hs"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@id = "list-con"]/a'):
            item = ZhiboItem()
            item['title'] = sel.xpath('h3/@title').extract()[0]
            item['link'] = sel.xpath('@href').extract()[0]
            num =  sel.xpath('ul/li[@class="livecard-meta-item livecard-meta-views"]/span[@class="livecard-meta-item-text"]/text()').extract()[0]
            item['view'] = self.webFunc.getNum(num)
            item['img_url'] = sel.xpath('img/@src').extract()[0]
            item['zhubo'] = sel.xpath('span/strong/text()').extract()[0]
            item['web'] = "longzhu"
            item['cate'] = "ls"
            # item['active'] = True
            yield item