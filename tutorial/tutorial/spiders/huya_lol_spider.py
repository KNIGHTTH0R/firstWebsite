import scrapy
import json
from tutorial.func import WebFunc
from tutorial.items import ZhiboItem

class QuanminSpider(scrapy.Spider):
    name = "huya_lol"
    webFunc = WebFunc(name)
    start_urls = [
        "http://www.huya.com/index.php?m=Game&do=ajaxGameLiveByPage&gid=1&page=1",
        "http://www.huya.com/index.php?m=Game&do=ajaxGameLiveByPage&gid=1&page=2",
        "http://www.huya.com/index.php?m=Game&do=ajaxGameLiveByPage&gid=1&page=3",
        "http://www.huya.com/index.php?m=Game&do=ajaxGameLiveByPage&gid=1&page=4",
        "http://www.huya.com/index.php?m=Game&do=ajaxGameLiveByPage&gid=1&page=5",
        "http://www.huya.com/index.php?m=Game&do=ajaxGameLiveByPage&gid=1&page=6"
    ]

    def parse(self, response):
        jsonBody = json.loads(response.body)
        for sel in jsonBody["data"]["list"]:
            num = self.webFunc.getNum(sel["totalCount"])
            if num >= self.webFunc.limit:
                item = ZhiboItem()
                # just slove the space character, need to be improved later
                item['title'] = sel["introduction"].replace("&nbsp;", " ")
                item['link'] = "http://www.huya.com/" + sel["privateHost"]
                item['view'] = num
                item['img_url'] = sel["screenshot"]
                item['zhubo'] = sel["nick"]
                item['web'] = "huya"
                item['cate'] = "lol"
                # item['active'] = True
                yield item