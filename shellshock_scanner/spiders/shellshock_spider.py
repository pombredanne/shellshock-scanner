# 3rd party modules
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

# Local project modules
from shellshock_scanner.items import ShellShockItem

domains_to_scan = [
    ('localhost', 8080),
]


class ShellshockSpider(CrawlSpider):
    name = 'shellshock'
    allowed_domains = [x[0] for x in domains_to_scan]
    start_urls = ['http://%s:%s/' % (x[0], x[1]) for x in domains_to_scan]

    rules = (
        Rule(LinkExtractor(allow=[]), callback='parse_start_url'),
    )

    def parse_start_url(self, response):
        item = ShellShockItem()
        item['url'] = response.url
        header = response.headers.get('x-shellshock-status')

        if header == 'vulnerable':
            item['vulnerable'] = True
            self.log('\033[91mURL "%s" is vulnerable\033[0m' % response.url)
        else:
            item['vulnerable'] = False

        return item
