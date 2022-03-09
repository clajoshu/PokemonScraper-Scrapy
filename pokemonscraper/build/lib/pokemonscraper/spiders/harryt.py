import scrapy


class HarrytSpider(scrapy.Spider):
    name = "harryt"
    start_urls = [
        'https://hairyt.com/collections/pokemon-sealed-product',
    ]

    def parse(self, response):
        for pokemon in response.css('div.productCard__card'):
            if pokemon.css('div.productCard__button.productCard__button--outOfStock::text').get() is None:
                yield {
                    'product_name': pokemon.css('p.productCard__title a::text').get().strip(),
                    'link': pokemon.css ('p.productCard__title a::attr(href)').get().strip(),
                    'price': pokemon.css('p.productCard__price::text').get().strip(),
                    'instock': pokemon.css('div.productCard__button.productCard__button--outOfStock::text').get(),
                }
   
        next_page = response.css('span.page a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)