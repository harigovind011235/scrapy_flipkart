import scrapy
from ..items import FlipkartItem


class FlipspiderSpider(scrapy.Spider):
    name = 'flipspider'

    start_urls = ['https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&page=1']

    def parse(self, response):

        myitems = FlipkartItem()

        data = response.css('div._1AtVbE')

        for mydata in data:

            mobname = mydata.css('div._4rR01T::text').extract()
            mobprice = mydata.css('._1_WHN1::text').extract()
            mobrating = mydata.css('._3LWZlK::text').extract()

            myitems['mob_name'] = mobname
            myitems['mob_price'] = mobprice
            myitems['mob_rating'] = mobrating

            yield myitems





