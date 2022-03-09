import scrapy


class PokemoncenterSpider(scrapy.Spider):
    name = "pokemoncenter"
    start_urls = [
        'https://www.pokemoncenter.com/en-ca/category/trading-card-game?sort=launch_date%2Bdesc',
        
    ]

    def parse(self, response):
        for pokemon in response.css('div._3O79ViVAyTDoy9CNAE24IM._3T1aZqusueKAoWk4GxF34M'):
            if pokemon.css('div._2nr0Etp6SAynnVo2b-ZoHr::text').get() is None:
                yield {
                    'product_name': pokemon.css ('h3.d6lLwC4dvdT-8RAAivZpR strong::text').get().strip(),
                    'link': pokemon.css ('div._3G36sDak6fTKioSv0frDai a::attr(href)').get().strip(),
                    'price': pokemon.css ('span.eCcSO0CxfOi-i5KfMoAxr::text').get(),
                    'instock': pokemon.css('div._2nr0Etp6SAynnVo2b-ZoHr::text').get(),
                }
   


        next_page = response.css('button.ItTc4bDy4l3wm76cQLQOI._2EgyS2JF4vSMMGt9KgAEkN._1DgNx-A1stl5GH9iL2A_el').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
