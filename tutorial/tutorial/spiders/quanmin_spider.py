import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem
from scrapy_splash import SplashRequest

class DouyuSpider(scrapy.Spider):
    name = "quanmin"
    webFunc = WebFunc()
    start_urls = [
        "http://www.quanmin.tv/game/hearthstone"
    ]

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.html', args=splash_args)

    def parse(self, response):
        for sel in response.xpath('//div[@class = "itemswrap"]/ul/li'):
            item = ZhiboItem()
            item['title'] = sel.xpath('a/img/@alt').extract()[0]
            item['link'] = "http://www.quanmin.tv" + sel.xpath('a[@class="subjectit"]/@href').extract()[0]
            num = sel.xpath('a/div/i[@class="nums ng-binding"]/text()').extract()[0]
            item['view'] = self.webFunc.getNum(num)
            item['img_url'] = sel.xpath('a/img/@ng-src').extract()[0]
            item['zhubo'] = sel.xpath('a/div/i[@class="zb ng-binding"]/text()').extract()[0]
            item['web'] = "quanmin"
            item['cate'] = "ls"
            # item['active'] = True
            yield item