# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class TiebaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question=Field()
    favour=Field()
    user=Field()
    user_info=Field()
    content=Field()
    pass
