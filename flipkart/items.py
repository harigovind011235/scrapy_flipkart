# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):

    mob_name = scrapy.Field()
    mob_price = scrapy.Field()
    mob_rating = scrapy.Field()

