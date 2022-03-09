import scrapy


class ThecomicwarehouseSpider(scrapy.Spider):
    name = "Thecomicwarehouse"
    custom_settings = {"FEEDS":{"thecomicwarehouse.csv":{"format":"csv"}}}
    start_urls = [
        'https://thecomicwarehouse.myshopify.com/collections/pokemon-card-game',
    ]

    def parse(self, response):
        for pokemon in response.css('div.grid__item.grid-product.medium--one-half.large--one-sixth'):
            if pokemon.css('div.grid-product__sold-out p::text').get() is None:
                yield {
                    'product_name': pokemon.css('span.grid-product__title::text').get().strip(),
                    'link': pokemon.css ('a.grid-product__meta::attr(href)').get().strip(),
                    'price': pokemon.xpath('//*[@class="long-dash"]//following-sibling::*').get()[140:-20].strip(),
                    'instock': pokemon.css('div.grid-product__sold-out p::text').get(),
                }        

        next_page = response.css('li.pagination--next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
