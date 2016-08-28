import scrapy

from scrapy import FormRequest
from LPJK.items import LpjkItem
from scrapy.shell import inspect_response
from scrapy.loader import ItemLoader

class LpjkSpider(scrapy.Spider):
    name = "lpjk"
    allowed_domains = ["http://lpjk.net"]
    start_urls = [
        "http://lpjk.net/status-proses-registrasi-badan-usaha-kbli-lpjk",
    ]

    def parse(self, response):
        propinsi = response.xpath('//select[@name="propinsi"]//@value').extract()
        for i in propinsi:
            yield FormRequest.from_response(
                response,
                formxpath = '//form[@name="demo1"]',
                formdata = {
                    'propinsi': i,
                },
                callback = self.parse_table,
                dont_filter = True
            )

    def parse_page(self, response):
        pages = response.xpath('//select[@name="page"]/option/text()').extract()
        for p in pages:
        yield FormRequest.from_response(
            response,
            formxpath = '//form[@action="status-proses-registrasi-badan-usaha-kbli-lpjk"]',
            formdata = {
                'page': p,
            },
            callback = self.parse_table,
            dont_filter = True
        )
           
    def parse_table(self, response):
        l = ItemLoader(item = LpjkItem(), response = response)
        l.add_xpath('num', '//blockquote/table[@class="text"]//tr/td[1]//text()')
        l.add_xpath('npwp', '//blockquote/table[@class="text"]//tr/td[2]//text()')
        l.add_xpath('tgl_permohonan', '//blockquote/table[@class="text"]//tr/td[3]//text()')
        l.add_xpath('tgl_diterima', '//blockquote/table[@class="text"]//tr/td[4]//text()')
        l.add_xpath('name', '//blockquote/table[@class="text"]//tr/td[5]//text()')
        l.add_xpath('proses', '//blockquote/table[@class="text"]//tr/td[6]//text()')
        l.add_xpath('status', '//blockquote/table[@class="text"]//tr/td[7]//text()')
        print(l.load_item())
        return l.load_item()

    def parse2(self, response):
        inspect_response(response, self)
           