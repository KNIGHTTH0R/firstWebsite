import scrapy

from tutorial.items import ZhiboItem

class HuyaSpider(scrapy.Spider):
    name = "huya"
    start_urls = [
        "http://www.huya.com/g/hearthstone"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class = "video-unit"]/ul/li'):
            item = ZhiboItem()
            item['title'] = sel.xpath('div/a/text()').extract()[0]
            item['link'] = sel.xpath('a/@href').extract()[0]
            num = sel.xpath('span[@class ="txt all_live_txt"]/span[@class="num"]/i/text()').extract()[0]
            item['view'] = num
            item['img_url'] = sel.xpath('a//img/@src').extract()[0]
            item['zhubo'] = sel.xpath('a//img/@title').extract()[0]
            item['web'] = "huya"
            item['cate'] = "ls"
            # item['active'] = True
            yield item