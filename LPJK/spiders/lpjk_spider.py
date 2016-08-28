import scrapy

from scrapy import FormRequest
from LPJK.items import LpjkItem
from scrapy.shell import inspect_response

class LpjkSpider(scrapy.Spider):
    name = "lpjk"
    allowed_domains = ["http://lpjk.net"]
    start_urls = [
        "http://lpjk.net/status-proses-registrasi-badan-usaha-kbli-lpjk",
    ]

    def parse(self, response):
        propinsi = response.xpath('//select[@name="propinsi"]//@value').extract()
        
        for i in propinsi:
            #for p in pages:
            yield FormRequest.from_response(
                response,
                formxpath = '//form[@name="demo1"]',
                formdata = {
                    'propinsi': i,
                },
                callback = self.parse_page,
                dont_filter = True
            )
           
    def parse_table(self, response):
        for sel in response:
            item = LpjkItem()
            item['item'] = sel.xpath('//table[@class="text"]//td/text()').extract()
            print("Inside Parse")
            yield item

    def parse_page(self, response):
        pages = response.xpath('//select[@name="page"]/@value').extract()
        for p in pages:
            yield FormRequest.from_response(
                response,
                formxpath = '//form[@action=""status-proses-registrasi-badan-usaha-kbli-lpjk""]',
                formdata = {
                    'page': p,
                },
                callback = self.parse2,
                dont_filter = True
            )
    
    def parse2(self,response):
        inspect_response(response, self)