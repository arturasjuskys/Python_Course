import scrapy

class BookSpider(scarpy.Spider):
	name = 'booksspider'
	start_utls = ['http://books.toscape.com']
	
	def parse(self, response):    #    <<<===    response: will be generated with start_urls variable
		for article in response.css('article.product_pod'):
			yield {
				'price': article.css(".price_color::text").extract_first(),
				'title': article.css("h3 > a::attr(title)").extract_first()
			}
			next = response.css('.next > a::attr(href)').extract_first()
			if next:
				yield response.follow(next, self.parse)
			
