#!/bin/sh
export PATH=$PATH:/usr/local/bin
cd /Users/wei/Documents/dawanfan/tutorial/
python /Users/wei/Documents/dawanfan/tutorial/tutorial/reset.py
scrapy crawl huya
scrapy crawl douyu
scrapy crawl panda
scrapy crawl zhanqi