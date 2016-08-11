import scrapy

from tutorial.items import ZhiboItem

class ZhanqiSpider(scrapy.Spider):
    name = "zhanqi"
    start_urls = [
        "http://www.zhanqi.tv/chns/blizzard/how"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class = "live-list-tabc tabc js-room-list-tabc" and not(p[@class = "no-videoList-title"])]/ul/li | //div[@class = "bb-hot-area bb-funny-area bb-room-list" or @class ="bb-variety-area bb-room-list"]/div[@class = "bd"]/ul/li | //div[@class = "video-list-tabc" and not(p[@class = "no-videoList-title"])]/ul/li'):
            item = ZhiboItem()
            item['title'] = sel.xpath('a/div[@class="imgBox"]/img/@alt').extract()[0]
            item['link'] = "http://www.zhanqi.tv" + sel.xpath('a/@href').extract()[0]
            num = sel.xpath('a/div[@class ="info-area"]/div[@class ="meat"]/span/span[@class = "dv"]/text()').extract()[0]
            item['view'] = num
            item['img_url'] = sel.xpath('a/div[@class="imgBox"]/img/@src').extract()[0]
            item['zhubo'] = sel.xpath('a/div[@class ="info-area"]/div[@class ="meat"]/span[@class = "anchor anchor-to-cut dv"]/text()').extract()[0]
            item['web'] = "zhanqi"
            item['cate'] = "ls"
            # item['active'] = True
            yield item