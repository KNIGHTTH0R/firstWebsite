import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class DouyuSpider(scrapy.Spider):
    name = "longzhu"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()

    def parse(self, response):
        for sel in response.xpath('//div[@id = "list-con"]/a'):
            item = ZhiboItem()
            num = self.webFunc.getNum(sel.xpath('ul/li[@class="livecard-meta-item livecard-meta-views"]/span[@class="livecard-meta-item-text"]/text()').extract()[0])
            if num >= self.webFunc.limit:
                item['title'] = sel.xpath('h3/@title').extract()[0]
                item['link'] = sel.xpath('@href').extract()[0]
                item['view'] = num
                item['img_url'] = sel.xpath('img/@src').extract()[0]
                item['zhubo'] = sel.xpath('span/strong/text()').extract()[0]
                item['web'] = "longzhu"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item