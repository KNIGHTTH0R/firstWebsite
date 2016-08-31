import scrapy
import json
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class QuanminSpider(scrapy.Spider):
    name = "huomao"
    webFunc = WebFunc(name)
    start_urls = webFunc.getURL()
    def parse(self, response):
        jsonBody = json.loads(response.body)
        for sel in jsonBody["data"]["channelList"]:
            num = self.webFunc.getNum(sel["views"])
            if num >= self.webFunc.limit:
                item = ZhiboItem()
                item['title'] = sel["channel"]
                item['link'] = "http://www.huomao.com/" + sel["id"]
                item['view'] = num
                item['img_url'] = sel["image"]
                item['zhubo'] = sel["nickname"]
                item['web'] = "huomao"
                item['cate'] = self.webFunc.getCate(response.url)
                # item['active'] = True
                yield item