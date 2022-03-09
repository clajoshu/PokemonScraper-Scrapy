import scrapy

class QuotesSpider(scrapy.Spider):
    name = "401games"
    start_urls = [
        'https://store.401games.ca/collections/pokemon-1',
    ]

    def parse(self, response):
        for pokemon in response.css('div.box.product'):
            if pokemon.css('span.sold-out-label::text').get() is None:
                yield {
                    'product_name': pokemon.css('a.title::text').get().strip(),
                    'link': pokemon.css ('div.product-title a::attr(href)').get().strip(),
                    'price': pokemon.css('span.money::text').get(),
                    'discount-price': pokemon.css('span.price span:nth-child(2)::text').get(),
                    'instock': pokemon.css('span.label.sold-out::text').get(),
                }    

        next_page = response.css('span.page a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
