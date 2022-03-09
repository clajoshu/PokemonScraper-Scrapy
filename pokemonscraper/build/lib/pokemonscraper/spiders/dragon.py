import scrapy


class DragonSpider(scrapy.Spider):
    name = 'dragon'
    allowed_domains = ['https://dragontcg.crystalcommerce.com/catalog/pokemon_sealed_products__u/14763']
    start_urls = ['http://https://dragontcg.crystalcommerce.com/catalog/pokemon_sealed_products__u/14763/']

    def parse(self, response):
        pass
