# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from tutorial.items import Product


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

        # Extract links of itens
        Rule(LinkExtractor(
            restrict_xpaths='//ul[@role="main"]/a[@name="linkToProduct"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ItemLoader(item=Product, response=response)
        item.add_xpath('name', '//h1[@class="header-product__title"]/text()')
        item.add_xpath('description', '//div[@class="description__container-text"]/text()')
        item.add_xpath('price', '//span[@class="price-template__text"]/text()')
        item.add_value('last_updated', 'today')
        return item.load_item()
