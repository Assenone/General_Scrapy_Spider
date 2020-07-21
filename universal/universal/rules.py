from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from urllib.parse import urljoin

def process(href):
    hrefs = href[7:]
    return urljoin('https://travel.qunar.com/travelbook/note', hrefs)

def process_next(href):
    return urljoin('https:', href)

rules = {
    'qunar': (
        Rule(LinkExtractor(restrict_xpaths='/html/body/div/div/div/ul/li/h2/a'),
        callback='parse_item'),
    )
}