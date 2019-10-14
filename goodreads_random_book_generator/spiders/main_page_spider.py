import scrapy


class MainPageSpider(scrapy.Spider):
    name = "main page"

    def start_requests(self):
        url = 'https://www.goodreads.com/review/list/45519898-flinn?shelf=to-read'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        with open('result.html', 'wb') as f:
            f.write(response.body)
        self.log('Saved file')