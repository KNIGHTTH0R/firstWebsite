class WebFunc():
    def getNum(self, num):
        num = num.replace(",", "")
        try:
            return int(num)
        except:
            return int(float(num[:-1]) * 10000)