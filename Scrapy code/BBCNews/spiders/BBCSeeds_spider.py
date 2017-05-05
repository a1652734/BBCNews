import scrapy
from bs4 import BeautifulSoup
from BBCNews.items import *
import re

class BBCNewsSeedsSpider(scrapy.Spider):
	name = 'BBCseeds'
	start_urls = ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk']

	def parse(self, response):
		soup = BeautifulSoup(response.body, 'html.parser')

		for news in soup.find_all('item'):
			yield scrapy.Request(news.link.text, self.parse_detail)


	def parse_detail(self, response):
		item = BbcnewsItem()
		res = BeautifulSoup(response.body, 'html.parser')
		
		#remove javascript code form content 
		for x in res.find_all('script'):
			x.extract()
		
		# Catch exception to  be done
		item['title'] = res.select('h1')[0].text
		item['url'] = response.url
		item['content'] = res.select('.story-body__inner')[0].text

		# item['title'] = re.sub("'", r"\'", res.select('h1')[0].text)
		# item['content'] = re.sub("'", r"\'", item['content'])

		#logging
		
		return item