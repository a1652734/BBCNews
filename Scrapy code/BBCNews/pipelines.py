# -*- coding: utf-8 -*-

import sqlite3
from scrapy.exceptions import DropItem

class BbcnewsPipeline(object):
	def open_spider(self, spider):
		self.conn = sqlite3.connect('BBC.sqlite')
		self.cur = self.conn.cursor()
		self.cur.execute('create table if not exists bbcnews(title varchar(100), url varchar(100) UNIQUE, content text, id INTEGER PRIMARY KEY AUTOINCREMENT)')
	
	def close_spider(self, spider):
		self.conn.close()
	
	def process_item(self, item, spider):
		col = ','.join(item.keys())
		placeholders = ','.join(len(item) * '?')
		sql = 'insert into bbcnews({}) values({})'
		print sql.format(col, placeholders), item.values()
		# Catch exceptions to be done
		self.cur.execute(sql.format(col, placeholders), item.values())
		self.conn.commit()
		#logging
		return item

