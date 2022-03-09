import scrapy

class QuotesSpider(scrapy.Spider):
    name = "cardmem"
    start_urls = [
        'https://www.cardboardmemories.ca/collections/pokemon',
    ]

    def parse(self, response):
        for pokemon in response.css('div.productitem'):
            if pokemon.css('span.productitem--badge.badge--soldout::text').get() is None:
                yield {
                    'product_name': pokemon.css('h2.productitem--title a::text').get().strip(),
                    'link': pokemon.css ('h2.productitem--title a::attr(href)').get().strip(),
                    'price': pokemon.css('span.money::text').get().strip(),
                    'instock': pokemon.css('span.productitem--badge.badge--soldout::text').get(),
                }
 
        
            

        next_page = response.css('li.pagination--next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)