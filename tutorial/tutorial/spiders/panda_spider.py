import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class PandaSpider(scrapy.Spider):
    name = "panda"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()

    def parse(self, response):
        for sel in response.xpath('//div[@class = "list-container"]/ul/li'):
            item = ZhiboItem()
            num = self.webFunc.getNum(sel.xpath('a/div[@class="video-info"]/span[@class = "video-number"]/text()').extract()[0])
            if num >= self.webFunc.limit:
                item['title'] = sel.xpath('a//img/@alt').extract()[0]
                item['link'] = "http://www.panda.tv" + sel.xpath('a/@href').extract()[0]
                item['view'] = num
                item['img_url'] = sel.xpath('a//img/@data-original').extract()[0]
                item['zhubo'] = sel.xpath('a/div[@class = "video-info"]/span[@class = "video-nickname"]/text()').extract()[0]
                item['web'] = "panda"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item