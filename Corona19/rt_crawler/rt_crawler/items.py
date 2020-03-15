# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RTItem(scrapy.Item):
    confirmed_case = scrapy.Field();
    isolation_case = scrapy.Field();
    death_toll = scrapy.Field();