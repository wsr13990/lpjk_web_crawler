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
        # for i in propinsi:
        yield FormRequest.from_response(
            response,
            formxpath = '//form[@name="demo1"]',
            formdata = {
                'propinsi': "01",
            },
            callback = self.parse_page,
            dont_filter = True
        )

    def parse_page(self, response):
        pages = response.xpath('//select[@name="page"]/@value').extract()
        # for p in pages:
        yield FormRequest.from_response(
            response,
            formxpath = '//form[@action="status-proses-registrasi-badan-usaha-kbli-lpjk"]',
            formdata = {
                'page': "2",
            },
            callback = self.parse_table,
            dont_filter = True
        )
           
    def parse_table(self, response):
        item = LpjkItem()
        item['num'] = response.xpath('//blockquote/table[@class="text"]//tr/td[1]//text()').extract()
        item['npwp'] = response.xpath('//blockquote/table[@class="text"]//tr/td[2]//text()').extract()
        item['tgl_permohonan'] = response.xpath('//blockquote/table[@class="text"]//tr/td[3]//text()').extract()
        item['tgl_diterima'] = response.xpath('//blockquote/table[@class="text"]//tr/td[4]//text()').extract()
        item['name'] = response.xpath('//blockquote/table[@class="text"]//tr/td[5]//text()').extract()
        item['proses'] = response.xpath('//blockquote/table[@class="text"]//tr/td[6]//text()').extract()
        item['status'] = response.xpath('//blockquote/table[@class="text"]//tr/td[7]//text()').extract()
        yield item

    def parse2(self, response):
        inspect_response(response, self)
           