# -*- coding: utf-8 -*-
import scrapy
from ..items import FlipkartItem


class FlipkartspiderSpider(scrapy.Spider):
    name = 'flipkartspider'
    page_number = 2
    start_urls = ['https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi']

    def parse(self ,response ):
        items = FlipkartItem()
        all_items = response.css('')
        for response in all_items:
        
            product_name = response.css('._3wU53n').css('::text').extract()
            product_price = response.css('._2rQ-NK').css('::text').extract()
            product_rating = response.css('.hGSR34').css('::text').extract()
            product_storage = response.css('.tVe95H:nth-child(1)').css('::text').extract()
            product_display = response.css('.tVe95H:nth-child(2)').css('::text').extract()
            product_camera = response.css('.tVe95H:nth-child(3)').css('::text').extract()
            product_battery = response.css('.tVe95H:nth-child(4)').css('::text').extract()
        
        

            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_rating'] = product_rating
            items['product_storage'] = product_storage
            items['product_display'] = product_display
            items['product_camera'] = product_camera
            items['product_battery'] = product_battery

        yield items

        next_page = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page=' + str(FlipkartspiderSpider.page_number) + ''
        if FlipkartspiderSpider.page_number <= 10:
            FlipkartspiderSpider.page_number+= 1
            yield response.follow(next_page, callback =self.parse)
         
   