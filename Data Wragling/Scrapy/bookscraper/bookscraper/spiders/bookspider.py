from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        # Extract links for next pages
        Rule(LinkExtractor(restrict_css=".next > a"), follow=True),
        # Extract links for books and parse them
        Rule(LinkExtractor(restrict_css=".product_pod h3 > a"), callback="parse_book"),
    )

    def parse_book(self, response):
        yield {
            "title": response.css("div.product_main h1::text").get(),
            "price": response.css("p.price_color::text").get(),
            "availability": response.css("p.availability::text").get().strip(),
            "category": response.xpath(
                '//ul[@class="breadcrumb"]/li[3]/a/text()'
            ).get(),
            "rating": response.css("p.star-rating::attr(class)").get().split()[-1],
            "description": response.xpath(
                '//div[@id="product_description"]/following-sibling::p/text()'
            ).get(),
            "upc": response.xpath(
                '//table[@class="table table-striped"]/tr[1]/td/text()'
            ).get(),
            "product_type": response.xpath(
                '//table[@class="table table-striped"]/tr[2]/td/text()'
            ).get(),
            "price_excl_tax": response.xpath(
                '//table[@class="table table-striped"]/tr[3]/td/text()'
            ).get(),
            "price_incl_tax": response.xpath(
                '//table[@class="table table-striped"]/tr[4]/td/text()'
            ).get(),
            "tax": response.xpath(
                '//table[@class="table table-striped"]/tr[5]/td/text()'
            ).get(),
            "availability_num": response.xpath(
                '//table[@class="table table-striped"]/tr[6]/td/text()'
            ).get(),
            "num_reviews": response.xpath(
                '//table[@class="table table-striped"]/tr[7]/td/text()'
            ).get(),
            "image_url": response.urljoin(
                response.css("div.item.active img::attr(src)").get()
            ),
            "book_url": response.url,
        }
