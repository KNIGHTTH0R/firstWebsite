#!/bin/sh
export PATH=$PATH:/usr/local/bin
cd /var/www/html/firstWebsite/tutorial/
python /var/www/html/firstWebsite/tutorial/tutorial/reset.py
scrapy crawl huya
scrapy crawl douyu
scrapy crawl panda
scrapy crawl zhanqi
scrapy crawl quanmin
scrapy crawl huomao
scrapy crawl longzhu