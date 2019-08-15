# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from os.path import abspath


class OutputSpider(CSVFeedSpider):
    name = 'output'
    allowed_domains = ['localhost']
    start_urls = [f'file:////{abspath(".")}/output.csv']
    headers = ['Product Code', 'Best Competitor', 'Best Competitor Price Total', 'Best Competitor Price Shipping',
               'Best Competitor price without shipping', 'Our Price Total', 'Our Price Shipping',
               'Our Price without Shipping', 'Best Price without shipping', 'Our Rank', 'Our Rank Price',
               'Difference Total Price', 'Difference Shipping', 'Difference Price']
    delimiter = ','

    # Do any adaptations you need here
    # def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        i['product_code'] = row['Product Code']
        i['our_price_total'] = row['Our Price Total']
        i['our_rank_price'] = row['Our Rank Price']
        return i
