import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem
from scrapy_splash import SplashRequest

class DouyuSpider(scrapy.Spider):
    name = "huomao"
    webFunc = WebFunc()
    start_urls = [
        "http://www.huomao.com/channel/ls"
    ]

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.html', args=splash_args)    

    def parse(self, response):
        for sel in response.xpath('//div[@class = "list-smallbox" and a/div[@class="live-dnf"]]'):
            item = ZhiboItem()
            item['title'] = sel.xpath('a//em/text()').extract()[0]
            item['link'] = "http://www.huomao.com/" + sel.xpath('a/@href').extract()[0]
            num = sel.xpath('a//em/span/text()').extract()[0]
            item['view'] = self.webFunc.getNum(num)
            item['img_url'] = sel.xpath('a//img/@data-original').extract()[0]
            item['zhubo'] = sel.xpath('a/p/span/text()').extract()[0]
            item['web'] = "huomao"
            item['cate'] = "ls"
            # item['active'] = True
            yield item