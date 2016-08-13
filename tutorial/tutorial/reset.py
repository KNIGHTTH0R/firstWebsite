import MySQLdb

db = MySQLdb.connect("localhost","root","root","zhibo")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS HearthStones")
sql = """CREATE TABLE HearthStones (
		 id INT NOT NULL AUTO_INCREMENT,
         title  CHAR(200) NOT NULL,
         link  CHAR(200),
         view INT,  
         img_url CHAR(200),
         zhubo CHAR(200),
         web CHAR(20),
         cate CHAR(20),
         # active BOOLEAN,
         PRIMARY KEY (id) )ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
cursor.execute(sql)