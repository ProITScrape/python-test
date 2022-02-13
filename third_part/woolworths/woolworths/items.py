# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WoolworthsItem(scrapy.Item):
    Products = scrapy.Field()
    Breadcrumb = scrapy.Field()