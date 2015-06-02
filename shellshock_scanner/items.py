# 3rd party modules
import scrapy


class ShellShockItem(scrapy.Item):
    url = scrapy.Field()
    vulnerable = scrapy.Field()
