# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LpjkItem(scrapy.Item):
    item = scrapy.Field()

class NavigationItem(scrapy.Item):
    propinsi = scrapy.Field()
