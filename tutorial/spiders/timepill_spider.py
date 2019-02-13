import scrapy



class QuotesSpider(scrapy.Spider):
    name = "time_pill"
    start_urls = [
        'http://www.timepill.net/'
        # 'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for diary in response.css('.diary'):
            yield {
                'use': diary.css('.icon::attr(href)').extract_first(),
                'img': diary.css('a img::attr(src)').extract_first(),
                'nickname': diary.css('.body .name::text').extract_first(),
                'book': diary.css('.body .title .book::attr(href)').extract_first(),
                'bookname': diary.css('.body .title .book::text').extract_first(),
                'time': str(diary.css('.body .title::text').extract()[1]).strip(),
            }
        next = response.css('#next a::attr(href)').extract_first()
        # if next is not None:
        #     next_page = response.urljoin(next)
        #     yield scrapy.Request(next_page, callback=self.parse)

