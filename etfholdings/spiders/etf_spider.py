import scrapy
from scrapy.selector import HtmlXPathSelector
from etfholdings import io

class ETFSpider(scrapy.Spider):
    """
    Parses etfdailynews, e.g.:
        view-source:https://etfdailynews.com/etf/QQQ/

    This site is good because it shows all the holdings in the HTML even though it uses table css/javascript to restrict the view in the browser
    """
    name = "ETF_Daily_News"

    start_urls = io.get_input_etfs()

    def parse(self, response):
        items = []

        #<table data-toggle="table" data-classes="striped" data-striped="true" data-pagination="true" data-page-size="10" data-mobile-responsive="true" class="table-condensed table table-striped news" id="etfs-that-own">
        T = response.xpath('//table[@data-toggle="table" and @data-classes="striped" and @data-striped="true" and @data-pagination="true" and @data-page-size="10" and @data-mobile-responsive="true" and @class="table-condensed table table-striped news"  and @id="etfs-that-own"]//tbody//tr')

        for r in T:
            rows = r.xpath('td')
            symbol = rows[0].xpath('a/text()').extract()[0]
            long_name = rows[1].xpath('a/text()').extract()[0]
            percent_allocation = rows[2].xpath('text()').extract()[0]
            items.append((symbol, long_name, percent_allocation))

        print(response)
        print(items)


