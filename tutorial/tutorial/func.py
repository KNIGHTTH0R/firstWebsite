class WebFunc():
    def getNum(self, num):
        try:
            return int(num)
        except:
            return int(float(num[:-1]) * 10000)