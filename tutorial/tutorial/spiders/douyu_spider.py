import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class DouyuSpider(scrapy.Spider):
    name = "douyu"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()

    def parse(self, response):
        for sel in response.xpath('//div[@id = "live-list-content"]/ul/li'):
            num =  self.webFunc.getNum(sel.xpath('a//span[@class="dy-num fr"]/text()').extract()[0])
            if num >= self.webFunc.limit:
                item = ZhiboItem()               
                item['title'] = sel.xpath('a/@title').extract()[0]
                item['link'] = "http://www.douyutv.com" + sel.xpath('a/@href').extract()[0]
                item['view'] = num
                item['img_url'] = sel.xpath('a//span[@class = "imgbox"]/img/@data-original').extract()[0]
                item['zhubo'] = sel.xpath('a//span[@class = "dy-name ellipsis fl"]/text()').extract()[0]
                item['web'] = "douyu"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item