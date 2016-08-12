# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import json
import codecs
import MySQLdb

class TutorialPipeline(object):
    def __init__(self):
        self.file = codecs.open('douyu.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MysqlPipeline(object):
	def __init__(self):
		self.db = MySQLdb.connect("localhost","root","root","zhibo")
		# ,charset ='utf8',use_unicode=True
		self.cursor = self.db.cursor()
		# self.cursor.execute("DROP TABLE IF EXISTS HearthStones")
		# sql = """CREATE TABLE HearthStones (
		# 		 id INT NOT NULL AUTO_INCREMENT,
		#          title  CHAR(200) NOT NULL,
		#          link  CHAR(200),
		#          view CHAR(200),  
		#          img_url CHAR(200),
		#          zhubo CHAR(200),
		#          web CHAR(20),
		#          cate CHAR(20),
		#          # active BOOLEAN,
		#          PRIMARY KEY (id) )"""
		# self.cursor.execute(sql)
	def process_item(self, item, spider):
		self.cursor.execute("INSERT INTO HearthStones(title, link, view, img_url, zhubo, web, cate) \
         		  			VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['title'], item['link'], item['view'], item['img_url'], item['zhubo'], item['web'], item['cate']))
		self.db.commit()
	def spider_closed(self, spider):
		self.db.close()