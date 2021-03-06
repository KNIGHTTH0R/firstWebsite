class WebFunc():
    cate = ["hs", "lol", "dota", "ow", "sc", "dnf", "girl"]
    urls = {
        'douyu' : ["How", "LOL", "DOTA2", "Overwatch", "SC", "DNF", "yz"],
        'huomao' : ["ls", "lol", "dota2", "Overwatch", "sc2", "DNF", "ylxx"],
        'huya' : ["hearthstone", "", "dota2", "2174", "starcraft", "dnf", "xingxiu"],
        'longzhu' : ["hs", "lol", "", "ow", "sc", "dnf", "lzxx"],
        'panda' : ["hearthstone", "lol", "dota2", "overwatch", "starcraft", "dnf", "yzdr"],
        'quanmin' : ["heartstone/list.json", "lol/list.json", "dota2/list.json", "overwatch/list.json", "", "dnf/list.json", "beauty/list.json"],
        'zhanqi' : ["chns/blizzard/how", "games/lol", "games/dota2", "chns/blizzard/watch", "chns/blizzard/sc2", "games/dnf", ""],
        'twitch' : ["Hearthstone%3A+Heroes+of+Warcraft", "League+of+Legends", "Dota+2", "Overwatch", "StarCraft+II", "Dungeon+Fighter+Online", ""]
    }
    prefix = {
        'douyu' : "https://www.douyu.com/directory/game/",
        'huomao' : "http://www.huomao.com/channels/channel.json?game_url_rule=",
        'huya' : "http://www.huya.com/g/",
        'longzhu' : "http://longzhu.com/channels/",
        'panda' : "http://www.panda.tv/cate/",
        'quanmin' : "http://www.quanmin.tv/json/categories/",
        'zhanqi' : "http://www.zhanqi.tv/",
        'twitch' : "https://streams.twitch.tv/kraken/streams?limit=60&offset=0&game="
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