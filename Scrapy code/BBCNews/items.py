# -*- coding: utf-8 -*-

import scrapy


class BbcnewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
