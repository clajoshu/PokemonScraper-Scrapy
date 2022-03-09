import scrapy
#from scrapy_selenium import SeleniumRequest
#from scrapy.linkextractors import LinkExtractor

class PokemoncenterSpider(scrapy.Spider):
    name = "pokemoncenter"
    
    custom_settings = {"FEEDS":{"pokemoncenter.csv":{"format":"csv"}}}
    def start_requests(self):
        urls = [
    
        'https://www.pokemoncenter.com/en-ca/category/trading-card-game?sort=launch_date%2Bdesc&ps=90&page=1',
        'https://www.pokemoncenter.com/en-ca/category/trading-card-game?sort=launch_date%2Bdesc&ps=90&page=2',
        'https://www.pokemoncenter.com/en-ca/category/trading-card-game?sort=launch_date%2Bdesc&ps=90&page=3',
        'https://www.pokemoncenter.com/en-ca/category/trading-card-game?sort=launch_date%2Bdesc&ps=90&page=4',
        'https://www.pokemoncenter.com/en-ca/category/trading-card-game?sort=launch_date%2Bdesc&ps=90&page=5',
        'https://www.pokemoncenter.com/en-ca/category/trading-card-game?sort=launch_date%2Bdesc&ps=90&page=6',
    ]
    
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for pokemon in response.css('div._3G36sDak6fTKioSv0frDai'):
            if pokemon.css('div._2nr0Etp6SAynnVo2b-ZoHr::text').get():
                yield {
                'product_name': pokemon.css ('h3.d6lLwC4dvdT-8RAAivZpR::text').get().strip(),
                'link': pokemon.css ('div._3G36sDak6fTKioSv0frDai a::attr(href)').get().strip(),
                'price': pokemon.css ('span.eCcSO0CxfOi-i5KfMoAxr::text').get(),
                'instock': pokemon.css('div._2nr0Etp6SAynnVo2b-ZoHr::text').get(),
            }
   

        #next_page = response.css('button.ItTc4bDy4l3wm76cQLQOI._2EgyS2JF4vSMMGt9KgAEkN._1DgNx-A1stl5GH9iL2A_el').get()
        #if next_page is not None:
         #   yield SeleniumRequest(next_page, callback=self.parse_result)
       # next_page = LinkExtractor(restrict_css='.> button').extract_links(response)[0]
        #if next_page.url is not None:
        #    yield response.follow(next_page, callback=self.parse)