import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class ZhanqiSpider(scrapy.Spider):
    name = "zhanqi"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()

    def parse(self, response):
        for sel in response.xpath('//div[@class = "live-list-tabc tabc js-room-list-tabc" and not(p[@class = "no-videoList-title"])]/ul/li | //div[@class = "bb-hot-area bb-funny-area bb-room-list" or @class ="bb-variety-area bb-room-list"]/div[@class = "bd"]/ul/li | //div[@class = "video-list-tabc" and not(p[@class = "no-videoList-title"])]/ul/li'):
            item = ZhiboItem()
            num = self.webFunc.getNum(sel.xpath('a/div[@class ="info-area"]/div[@class ="meat"]/span/span[@class = "dv"]/text()').extract()[0])
            if num >= self.webFunc.limit:
                item['title'] = sel.xpath('a/div[@class="imgBox"]/img/@alt').extract()[0]
                item['link'] = "http://www.zhanqi.tv" + sel.xpath('a/@href').extract()[0]
                item['view'] = num
                item['img_url'] = sel.xpath('a/div[@class="imgBox"]/img/@src').extract()[0]
                item['zhubo'] = sel.xpath('a/div[@class ="info-area"]/div[@class ="meat"]/span[@class = "anchor anchor-to-cut dv"]/text()').extract()[0]
                item['web'] = "zhanqi"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item