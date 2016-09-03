import scrapy
import json
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class QuanminSpider(scrapy.Spider):
    name = "twitch"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()

    def parse(self, response):
        jsonBody = json.loads(response.body)
        for sel in jsonBody["streams"]:
            num = self.webFunc.getNum(str(sel["viewers"]))
            if num >= self.webFunc.limit:
                item = ZhiboItem()
                item['title'] = sel["channel"]["status"]
                item['link'] = sel["channel"]["url"]
                item['view'] = num
                item['img_url'] = sel["preview"]["medium"]
                item['zhubo'] = sel["channel"]["display_name"]
                item['web'] = "twitch"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item