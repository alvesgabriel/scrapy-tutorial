# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MagazineluizaSpider(CrawlSpider):
    name = 'magazineluiza'
    allowed_domains = ['magazineluiza.com.br']
    start_urls = ['http://magazineluiza.com.br/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Extract links with xpath to categories
        Rule(LinkExtractor(restrict_xpaths='//li[@class="item-of-menu"]/a')),

        # Extract links with xpath to subcategories
        Rule(LinkExtractor(
            restrict_xpaths='//div[@class="block-left-menu "]/ul[@class="container-menu-side block-line-menu-left"]/li/a')),

        # Extract links of pagination
        Rule(LinkExtractor(
            restrict_xpaths='//li/a[@role="button" and starts-with(@aria-label,"Page ")]')),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
