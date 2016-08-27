import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem
from scrapy_splash import SplashRequest

class QuanminSpider(scrapy.Spider):
    name = "quanmin"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()

    def start_requests(self):
        splash_args = {
            'wait': 2.0, 'images' : 0
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.html', args=splash_args)

    def parse(self, response):
        for sel in response.xpath('//div[@class = "itemswrap"]/ul/li'):
            num = self.webFunc.getNum(sel.xpath('a/div/i[@class="nums ng-binding"]/text()').extract()[0])
            if num >= self.webFunc.limit:
                item = ZhiboItem()
                item['title'] = sel.xpath('a/img/@alt').extract()[0]
                item['link'] = "http://www.quanmin.tv" + sel.xpath('a[@class="subjectit"]/@href').extract()[0]
                item['view'] = num
                item['img_url'] = sel.xpath('a/img/@ng-src').extract()[0]
                item['zhubo'] = sel.xpath('a/div/i[@class="zb ng-binding"]/text()').extract()[0]
                item['web'] = "quanmin"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item