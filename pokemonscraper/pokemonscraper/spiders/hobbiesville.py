import scrapy

class QuotesSpider(scrapy.Spider):
    name = "hobbiesville"
    custom_settings = {"FEEDS":{"hobbiesville.csv":{"format":"csv"}}}
    start_urls = [
        'https://hobbiesville.com/collections/pokemon-trading-cards/categories_trading-cards?sort_by=created-descending',
    ]

    def parse(self, response):
        for pokemon in response.css('div.collectionBlock.js-collectionBlock.block.lg_s15.med_s13.s12'):
            if pokemon.css('span.sold-out-label::text').get() is None:
                yield {

                    'product_name': pokemon.css('h3:nth-child(2) a::text').get().strip(),
                    'picture': pokemon.css('div.collectionBlock.js-collectionBlock.block.lg_s15.med_s13.s12 div::attr(style)').get(),
                    'link': pokemon.css ('h3:nth-child(2) a::attr(href)').get().strip(),
                    'price': pokemon.css('span.money::text').get(),
                    'instock': pokemon.css('span.sold-out-label::text').get(),
                }
        

        next_page = response.css('div.pagination span.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)