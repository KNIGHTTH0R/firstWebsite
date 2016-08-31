import scrapy
import json
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class QuanminSpider(scrapy.Spider):
    name = "quanmin"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()

    def parse(self, response):
        jsonBody = json.loads(response.body)
        for sel in jsonBody["data"]:
            num = self.webFunc.getNum(sel["view"])
            if num >= self.webFunc.limit:
                item = ZhiboItem()
                item['title'] = sel["title"]
                item['link'] = "http://www.quanmin.tv/v/" + sel["uid"]
                item['view'] = num
                item['img_url'] = sel["thumb"]
                item['zhubo'] = sel["nick"]
                item['web'] = "quanmin"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item