import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        if self.tag is not None:
            url = url + 'tag/' + self.tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)
