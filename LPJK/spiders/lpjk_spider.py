import scrapy

from scrapy import FormRequest
from LPJK.items import LpjkItem
from LPJK.items import NavigationItem

class LpjkSpider(scrapy.Spider):
    name = "lpjk"
    allowed_domains = ["http://lpjk.net"]
    start_urls = [
        "http://lpjk.net/status-proses-registrasi-badan-usaha-kbli-lpjk",
    ]

    def parse(self, response):
        print (response)
        propinsi = response.xpath('//select[@name="propinsi"]//@value').extract()
        for i in propinsi:
            return FormRequest.from_response(
                response,
                formxpath = '//form[@name="demo1"]',
                formdata = {
                    'propinsi':i,
                },
                callback = self.parse_table
            )
            #print(scrapy.Request(response, callback=parse_table))
                

    def parse_link(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            ulr = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_table)
           
    def parse_table(self, response):
        for sel in response:
            item = LpjkItem()
            item['item'] = sel.xpath('//table[@class="text"]//td/text()').extract()
            print("Inside Parse")
            yield item