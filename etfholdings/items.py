# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class EtfholdingsItem(scrapy.Item):
    # define the fields for your item here like:
    fund = scrapy.Field()
    symbol = scrapy.Field()
    long_name = scrapy.Field()
    percentage_allocation = scrapy.Field()
