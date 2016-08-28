import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class HuyaSpider(scrapy.Spider):
    name = "huya"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()

    def parse(self, response):
        for sel in response.xpath('//div[@class = "video-wrap"]//ul/li'):
            num =  self.webFunc.getNum(sel.xpath('div/span[@class="num"]//text() | span/span[@class="num"]//text()').extract()[0])
            if num >= self.webFunc.limit:
                item = ZhiboItem()
                item['title'] = sel.xpath('div//a/text()').extract()[0]
                item['link'] = sel.xpath('a/@href').extract()[0]
                item['view'] = num
                item['img_url'] = sel.xpath('a//img/@src').extract()[0]
                item['zhubo'] = sel.xpath('a//img/@title').extract()[0]
                item['web'] = "huya"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item