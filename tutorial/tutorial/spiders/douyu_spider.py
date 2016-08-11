import scrapy

from tutorial.items import ZhiboItem

class DouyuSpider(scrapy.Spider):
    name = "douyu"
    start_urls = [
        "http://www.douyu.com/directory/game/How"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@id = "live-list-content"]/ul/li'):
            item = ZhiboItem()
            item['title'] = sel.xpath('a/@title').extract()[0]
            item['link'] = "http://www.douyutv.com" + sel.xpath('a/@href').extract()[0]
            num =  sel.xpath('a//span[@class="dy-num fr"]/text()').extract()[0]
            item['view'] = num
            item['img_url'] = sel.xpath('a//span[@class = "imgbox"]/img/@data-original').extract()[0]
            item['zhubo'] = sel.xpath('a//span[@class = "dy-name ellipsis fl"]/text()').extract()[0]
            item['web'] = "douyu"
            item['cate'] = "ls"
            # item['active'] = True
            yield item