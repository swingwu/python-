from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from tieba.items import  TiebaItem

class tieba(CrawlSpider):
    name='tieba'
    start_urls=[]

    def parse(self, response):
        item=TiebaItem()
        selector=Selector(response)
        infos=selector.xpath('')
        for info in infos:
            try:
                question=info.xpath()
                favour=info.xpath()
                user=info.xpath()
                user_info=info.xpath()
                content=info.xpath()
                item['question']=question
                item['favour'] =favour
                item['user'] =user
                item['user_info'] =user_info
                item['content'] =content
                yield item
            except IndexError:
                pass

        urls=[''.format(str(i)) for i in range(2,50)]
        for url in urls:
            yield Request(url,callback=self.parse)#回调函数

