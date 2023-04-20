import scrapy


class ShephardspiderSpider(scrapy.Spider):
    name = "shephardSpider"
    allowed_domains = ["www.shephardmedia.com"]
    start_urls = ["https://www.shephardmedia.com/news/?page=1"]

    def parse(self, response):
        storiesCategory = response.xpath('//section[@class="article-list"]//ul/li//h4//a')
        for row in storiesCategory:
            categoryText = row.xpath('./text()').get()
            print(categoryText)
        storiesTitle = response.xpath('//section[@class="article-list"]//ul/li//h2//a')
        for row in storiesTitle:
            title = row.xpath('./text()').get()
            print(title)
        storiesDate = response.xpath('//section[@class="article-list"]//ul/li//p[@class="date"]')
        for row in storiesDate:
            dateText = row.xpath('./text()').get()
            print(dateText)

  
    pass
