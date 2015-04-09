# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://news.dbanotes.net/"
    ]

# startup new 爬虫
    def parse(self, response):
        for sel in response.xpath('//tr/td//tr'):
            item = DmozItem()
            item['id'] = sel.xpath('td/text()[1]').re('\d+')
            item['title'] = sel.xpath('td[3]/a/text()').extract()
            item['link'] = sel.xpath('td[3]/a/@href').extract()
            yield item
