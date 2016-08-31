import scrapy
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class ZhanqiSpider(scrapy.Spider):
    name = "zhanqi_girl"
    webFunc = WebFunc(name)
    start_urls = ["http://bb.zhanqi.tv/"]

    def parse(self, response):
        for sel in response.xpath('//div[@class = "bb-variety-area bb-room-list"]/div[@class = "bd"]/ul/li'):
            item = ZhiboItem()
            num = self.webFunc.getNum(sel.xpath('a/div[@class="info-area"]/div/span/span/text()').extract()[0])
            if num >= self.webFunc.limit:
                item['title'] = sel.xpath('a/div[@class="sub-mask"]/p/text()').extract()[0]
                item['link'] = "http://www.zhanqi.tv" + sel.xpath('a/@href').extract()[0]
                item['view'] = num
                item['img_url'] = sel.xpath('a/div[@class="imgBox"]/img/@src').extract()[0]
                item['zhubo'] = sel.xpath('a/div[@class="imgBox"]/img/@alt').extract()[0]
                item['web'] = "zhanqi"
                item['cate'] = "girl"
                # item['active'] = True
                yield item