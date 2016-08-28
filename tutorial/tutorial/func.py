class WebFunc():
    cate = ["hs", "lol", "dota", "ow", "sc", "dnf"]
    urls = {
        'douyu' : ["How", "LOL", "DOTA2", "Overwatch", "SC", "DNF"],
        'huomao' : ["ls", "lol", "dota2", "Overwatch", "sc2", "DNF"],
        'huya' : ["hearthstone", "", "dota2", "2174", "starcraft", "dnf"],
        'longzhu' : ["hs", "lol", "", "ow", "sc", "dnf"],
        'panda' : ["hearthstone", "lol", "dota2", "overwatch", "starcraft", "dnf"],
        'quanmin' : ["hearthstone", "lol", "dota2", "overwatch", "", "dnf"],
        'zhanqi' : ["chns/blizzard/how", "games/lol", "games/dota2", "chns/blizzard/watch", "chns/blizzard/sc2", "games/dnf"]
    }
    prefix = {
        'douyu' : "http://www.douyu.com/directory/game/",
        'huomao' : "http://www.huomao.com/channel/",
        'huya' : "http://www.huya.com/g/",
        'longzhu' : "http://longzhu.com/channels/",
        'panda' : "http://www.panda.tv/cate/",
        'quanmin' : "http://www.quanmin.tv/game/",
        'zhanqi' : "http://www.zhanqi.tv/"
    }
    web_name = ''
    limit = 100

    def __init__(self, name):
        self.web_name = name

    # get the complete urls for each web site
    def getURL(self):       
        completeURL = []
        for url in self.urls[self.web_name]:
            if url:
                completeURL.append(self.prefix[self.web_name] + url)
        return completeURL

    # get the category of the correspoding URL
    def getCate(self, completeURL):
        length = len(self.prefix[self.web_name])
        url = completeURL[length:]
        return self.cate[self.urls[self.web_name].index(url)]

    def getNum(self, num):
        num = num.replace(",", "")
        try:
            return int(num)
        except:
            return int(float(num[:-1]) * 10000)