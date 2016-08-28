# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags, replace_escape_chars
from scrapy.loader.processors import Join, MapCompose, TakeFirst

def clean_escape_char(x):
    x = [x.strip("\r\n\t\t\t")]
    return x

class LpjkItem(scrapy.Item):
    num = scrapy.Field()
    npwp = scrapy.Field()
    tgl_permohonan = scrapy.Field()
    tgl_diterima = scrapy.Field()
    name = scrapy.Field()
    proses = scrapy.Field()
    status = scrapy.Field(
        input_processor= MapCompose(clean_escape_char),
    )


