import scrapy


class ZephyrSpider(scrapy.Spider):
    name = "zephyr"
    start_urls = [
        'https://zephyrepic.com/shop/category/trading-card-games/pokemon/?',
    ]

    def parse(self, response):
        for pokemon in response.css('main.grid__item.one-whole.lg-three-quarters'):
            #if pokemon.css('span.product-tag.product-tag--no-stock::text').get() is None:
            yield {
                'product_name': pokemon.css('h3.delta.trailer--half::text').get(),
                'link': pokemon.css ('a.card.card--product a::attr(href)').get(),
                'price': pokemon.css('span.woocommerce-Price-amount.amount bdi::text').get(),
                'instock': pokemon.css('span.product-tag.product-tag--no-stock::text').get(),
            }
            

        next_page = response.css('a.pagination--item::attr(href)').get()
        if next_page:
            yield scrapy.request(
                response.urljoin(next_page),
                callback=self.parse
            )