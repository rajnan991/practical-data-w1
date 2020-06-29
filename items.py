# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_rating = scrapy.Field()
    product_storage = scrapy.Field()
    product_display = scrapy.Field()
    product_camera = scrapy.Field()
    product_battery = scrapy.Field()
    
    
