"""
MEGA SCRAPY TEMPLATE
====================

This template provides a comprehensive framework for building flexible web scrapers
with Scrapy that can be adapted to various websites with minimal modifications.

Features:
- Pagination handling
- Login capability
- Item processing
- Data cleaning
- Proxy rotation
- User-agent rotation
- Rate limiting
- Handling JavaScript-rendered pages
- Error handling and retries
- Export to multiple formats
- Logging and monitoring

Usage:
1. Customize the spider class with your target website details
2. Configure the settings as needed
3. Run with: scrapy crawl mega_spider -o data.csv

"""

import datetime
import json
import logging
import os
import random
import re
from urllib.parse import urljoin

import scrapy
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.http import FormRequest, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.spiders import CrawlSpider, Rule
from w3lib.html import remove_tags

#######################################
# ITEMS DEFINITION
#######################################


class GenericItem(scrapy.Item):
    """
    Generic item for storing scraped data.
    Add or remove fields as needed for your specific use case.
    """

    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()  # For the images pipeline
    category = scrapy.Field()
    tags = scrapy.Field()
    author = scrapy.Field()
    date_published = scrapy.Field()
    rating = scrapy.Field()
    reviews_count = scrapy.Field()
    metadata = scrapy.Field()
    timestamp = scrapy.Field()
    extra_data = scrapy.Field()


#######################################
# ITEM LOADERS
#######################################


class GenericItemLoader(ItemLoader):
    """
    Item loader with common input/output processors
    """

    default_output_processor = TakeFirst()

    # Input processors
    title_in = MapCompose(str.strip, remove_tags)
    description_in = MapCompose(str.strip, remove_tags)
    price_in = MapCompose(
        str.strip, remove_tags, lambda x: x.replace("$", "").replace(",", "")
    )
    category_in = MapCompose(str.strip, remove_tags)
    tags_in = MapCompose(str.strip, remove_tags)
    author_in = MapCompose(str.strip, remove_tags)

    # Output processors
    description_out = Join()
    tags_out = lambda x: [tag.strip() for tag in x]
    price_out = TakeFirst()  # Take first value and try to convert to float
    image_urls_out = lambda x: [url for url in x if url]  # Filter None values


#######################################
# MIDDLEWARE AND PIPELINES
#######################################


class CleanDataPipeline:
    """
    Pipeline for cleaning and validating scraped data
    """

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Clean price (convert to float if possible)
        if adapter.get("price"):
            try:
                adapter["price"] = float(adapter["price"])
            except (ValueError, TypeError):
                spider.logger.warning(
                    f"Could not convert price to float: {adapter['price']}"
                )

        # Clean and standardize dates
        if adapter.get("date_published"):
            try:
                # Attempt to standardize date format
                date_str = adapter["date_published"]
                # Implement your date parsing logic here based on expected formats
                # This is a simple example assuming ISO format
                date_obj = datetime.datetime.fromisoformat(
                    date_str.replace("Z", "+00:00")
                )
                adapter["date_published"] = date_obj.isoformat()
            except Exception as e:
                spider.logger.warning(f"Date parsing error: {e}")

        # Add timestamp
        adapter["timestamp"] = datetime.datetime.utcnow().isoformat()

        # Validate required fields
        required_fields = ["url", "title"]  # Customize this as needed
        for field in required_fields:
            if not adapter.get(field):
                raise DropItem(f"Missing required field {field}")

        return item


class ImagePipeline:
    """
    Simple placeholder for an image pipeline.
    For actual image downloading, use Scrapy's built-in ImagesPipeline.
    """

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("image_urls"):
            # Typically, you'd configure Scrapy's ImagesPipeline in settings.py instead
            # This is just a placeholder for demonstration
            adapter["images"] = [
                {"url": url, "status": "pending"} for url in adapter["image_urls"]
            ]
        return item


class ProxyMiddleware:
    """
    Middleware for rotating proxies
    """

    def __init__(self, proxy_list):
        self.proxy_list = proxy_list
        self.current_proxy = None

    @classmethod
    def from_crawler(cls, crawler):
        # Get proxy list from settings or environment
        proxy_list = crawler.settings.get("PROXY_LIST", [])
        if not proxy_list and os.environ.get("PROXY_LIST"):
            proxy_list = os.environ.get("PROXY_LIST").split(",")
        return cls(proxy_list)

    def process_request(self, request, spider):
        if self.proxy_list:
            self.current_proxy = random.choice(self.proxy_list)
            request.meta["proxy"] = self.current_proxy
            spider.logger.debug(f"Using proxy: {self.current_proxy}")


class UserAgentMiddleware:
    """
    Middleware for rotating user agents
    """

    def __init__(self, user_agent_list):
        self.user_agent_list = user_agent_list

    @classmethod
    def from_crawler(cls, crawler):
        user_agent_list = crawler.settings.get(
            "USER_AGENT_LIST",
            [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
            ],
        )
        return cls(user_agent_list)

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agent_list)
        request.headers["User-Agent"] = user_agent
        spider.logger.debug(f"Using User-Agent: {user_agent}")


#######################################
# MAIN SPIDER
#######################################


class MegaSpider(CrawlSpider):
    """
    A comprehensive crawler spider that can be customized for different websites
    """

    name = "mega_spider"

    # CUSTOMIZE THESE FOR YOUR TARGET WEBSITE
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    # Login details (if needed)
    login_url = None  # e.g., 'https://example.com/login'
    login_user = None
    login_pass = None

    # Rules for following links
    rules = (
        # Follow pagination links
        Rule(LinkExtractor(restrict_css=".pagination a.next"), follow=True),
        # Follow category links
        Rule(LinkExtractor(restrict_css=".categories a"), follow=True),
        # Extract item links and parse them
        Rule(
            LinkExtractor(restrict_css=".product-item a.title"), callback="parse_item"
        ),
    )

    # CUSTOMIZE THESE SELECTORS FOR YOUR TARGET WEBSITE
    # These are examples and should be adjusted for your specific case
    item_selectors = {
        "title": '//h1[@class="product-title"]/text()',
        "price": '//span[@class="price"]/text()',
        "description": '//div[@class="description"]//text()',
        "image_urls": '//div[@class="product-images"]//img/@src',
        "category": '//ol[@class="breadcrumb"]/li[2]/a/text()',
        "tags": '//div[@class="tags"]//a/text()',
        "author": '//span[@class="author"]/text()',
        "date_published": '//meta[@name="date"]/@content',
        "rating": '//div[@class="rating"]/@data-rating',
        "reviews_count": '//span[@class="reviews-count"]/text()',
    }

    # REQUEST THROTTLING
    # Adjust these for polite scraping
    download_delay = 2  # 2 seconds between requests
    randomize_download_delay = True

    # CUSTOM SETTINGS
    custom_settings = {
        "CONCURRENT_REQUESTS": 4,  # Lower concurrency to be nicer to servers
        "RETRY_TIMES": 3,  # Number of retries for failed requests
        "RETRY_HTTP_CODES": [500, 502, 503, 504, 408, 429],  # Status codes to retry
        "ROBOTSTXT_OBEY": True,  # Respect robots.txt rules
        "COOKIES_ENABLED": True,  # Enable cookies
        "FEED_EXPORT_ENCODING": "utf-8",  # Ensure UTF-8 encoding for exports
        # Uncomment and modify these as needed
        # 'PROXY_LIST': ['http://proxy1.example.com', 'http://proxy2.example.com'],
        # 'DOWNLOADER_MIDDLEWARES': {
        #     '__main__.UserAgentMiddleware': 400,
        #     '__main__.ProxyMiddleware': 410,
        # },
        # 'ITEM_PIPELINES': {
        #     '__main__.CleanDataPipeline': 300,
        #     '__main__.ImagePipeline': 200,
        # },
    }

    def __init__(self, *args, **kwargs):
        """
        Initialize the spider with dynamic parameters
        """
        super(MegaSpider, self).__init__(*args, **kwargs)

        # Read credentials from environment variables if not set
        if not self.login_user and os.environ.get("SCRAPER_USER"):
            self.login_user = os.environ.get("SCRAPER_USER")
        if not self.login_pass and os.environ.get("SCRAPER_PASS"):
            self.login_pass = os.environ.get("SCRAPER_PASS")

        # You can add additional initialization logic here

    def start_requests(self):
        """
        Start requests method to handle login if needed
        """
        if self.login_url and self.login_user and self.login_pass:
            # If login information is available, start with login
            yield scrapy.Request(
                url=self.login_url, callback=self.login, dont_filter=True
            )
        else:
            # Otherwise, start with the regular start_urls
            for url in self.start_urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def login(self, response):
        """
        Handle login process
        Customize this method based on the login form structure
        """
        self.logger.info("Logging in...")

        # Extract any CSRF token if needed
        csrf_token = response.css('input[name="csrf_token"]::attr(value)').get()

        # Prepare form data
        formdata = {
            "username": self.login_user,
            "password": self.login_pass,
        }

        # Add CSRF token if found
        if csrf_token:
            formdata["csrf_token"] = csrf_token

        # Submit the login form
        return FormRequest.from_response(
            response, formdata=formdata, callback=self.after_login, dont_filter=True
        )

    def after_login(self, response):
        """
        Check if login was successful and continue crawling
        """
        # Check login success
        # Customize this check based on your target site
        if "Sign Out" in response.text or "Welcome" in response.text:
            self.logger.info("Login successful")
            # Continue with crawling the start URLs
            for url in self.start_urls:
                yield scrapy.Request(url=url, callback=self.parse)
        else:
            self.logger.error("Login failed")
            # You can still continue, but some content might be restricted
            for url in self.start_urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse_item(self, response):
        """
        Parse a product/item page
        """
        self.logger.info(f"Parsing item: {response.url}")

        # Use ItemLoader for cleaner data processing
        loader = GenericItemLoader(item=GenericItem(), response=response)

        # Load the URL
        loader.add_value("url", response.url)

        # Apply selectors for each field
        for field, selector in self.item_selectors.items():
            # Handle different selector types
            if selector.startswith("//"):  # XPath
                loader.add_xpath(field, selector)
            elif selector.startswith("."):  # CSS
                loader.add_css(field, selector)
            else:  # Assume CSS
                loader.add_css(field, selector)

        # Extract JSON-LD data if available (common for structured data)
        json_ld_data = self.extract_json_ld(response)
        if json_ld_data:
            loader.add_value("metadata", json_ld_data)

        # Handle image URLs - make them absolute
        if "image_urls" in loader.get_collected_values():
            image_urls = []
            for url in loader.get_collected_values("image_urls"):
                image_urls.append(urljoin(response.url, url))
            loader.replace_value("image_urls", image_urls)

        # Load item
        item = loader.load_item()

        # Yield the item
        yield item

    def extract_json_ld(self, response):
        """
        Extract JSON-LD structured data from the page
        """
        json_ld_script = response.xpath(
            '//script[@type="application/ld+json"]/text()'
        ).get()
        if json_ld_script:
            try:
                return json.loads(json_ld_script)
            except json.JSONDecodeError:
                self.logger.warning("Failed to parse JSON-LD data")
        return None

    def handle_javascript(self, response):
        """
        Handle JavaScript-rendered pages
        For full JS support, consider using Splash, Selenium, or Playwright
        """
        # This is a placeholder for sites that require JavaScript rendering
        # In a real implementation, you would use a JavaScript middleware
        # such as scrapy-splash, scrapy-selenium, or scrapy-playwright
        self.logger.info("JavaScript handling would happen here")
        return response

    def errback_handler(self, failure):
        """
        Handle request errors
        """
        request = failure.request
        self.logger.error(f"Request failed: {request.url}")

        if failure.check(scrapy.exceptions.IgnoreRequest):
            self.logger.warning(
                "IgnoreRequest error, possibly filtered by the OffsiteMiddleware"
            )
        elif failure.check(scrapy.exceptions.DNSLookupError):
            self.logger.error(f"DNSLookupError on {request.url}")
        elif failure.check(scrapy.exceptions.TimeoutError, TimeoutError):
            self.logger.error(f"TimeoutError on {request.url}")
        else:
            self.logger.error(f"Other error: {failure}")


#######################################
# SPIDER EXAMPLES
#######################################


class ExampleEcommerceSiteSpider(MegaSpider):
    """
    Example for an e-commerce site
    """

    name = "example_ecommerce"
    allowed_domains = ["fakeecommerce.com"]
    start_urls = ["https://fakeecommerce.com/products"]

    # E-commerce specific rules
    rules = (
        # Follow pagination links
        Rule(LinkExtractor(restrict_css=".pagination a.next"), follow=True),
        # Follow category links
        Rule(LinkExtractor(restrict_css=".category-menu a"), follow=True),
        # Extract product links and parse them
        Rule(
            LinkExtractor(restrict_css=".product-grid .product-item a.product-link"),
            callback="parse_item",
        ),
    )

    # E-commerce specific selectors
    item_selectors = {
        "title": '//h1[@class="product-title"]/text()',
        "price": '//span[@class="current-price"]/text()',
        "description": '//div[@class="product-description"]//text()',
        "image_urls": '//div[@class="product-gallery"]//img/@src',
        "category": '//nav[@class="breadcrumb"]/a[2]/text()',
        "rating": '//div[@class="product-rating"]/@data-rating',
        "reviews_count": '//span[@class="review-count"]/text()',
    }


class ExampleNewsSpider(MegaSpider):
    """
    Example for a news site
    """

    name = "example_news"
    allowed_domains = ["fakenews.com"]
    start_urls = ["https://fakenews.com/latest"]

    # News site specific rules
    rules = (
        # Follow pagination links
        Rule(LinkExtractor(restrict_css=".pagination a"), follow=True),
        # Follow category/section links
        Rule(LinkExtractor(restrict_css=".sections-menu a"), follow=True),
        # Extract article links and parse them
        Rule(
            LinkExtractor(restrict_css=".article-list .article-item a.headline"),
            callback="parse_item",
        ),
    )

    # News site specific selectors
    item_selectors = {
        "title": '//h1[@class="article-title"]/text()',
        "description": '//meta[@name="description"]/@content',
        "author": '//span[@class="author-name"]/text()',
        "date_published": '//meta[@property="article:published_time"]/@content',
        "category": '//div[@class="article-category"]/a/text()',
        "tags": '//div[@class="article-tags"]//a/text()',
        "image_urls": '//figure[@class="article-image"]//img/@src',
    }

    # Override to handle article content differently
    def parse_item(self, response):
        item = super().parse_item(response)

        # Add article content
        article_content = " ".join(response.css(".article-body p::text").getall())
        item.add_value("extra_data", {"article_content": article_content})

        return item


#######################################
# USAGE EXAMPLES
#######################################

# To run the spider from command line:
# scrapy runspider mega_scrapy_template.py -o data.csv -t csv

# For JSON output:
# scrapy runspider mega_scrapy_template.py -o data.json -t json

# To save multiple formats at once:
# scrapy runspider mega_scrapy_template.py -o data.csv -t csv -o data.json -t json

# To set custom settings:
# scrapy runspider mega_scrapy_template.py -s DOWNLOAD_DELAY=5 -s CONCURRENT_REQUESTS=2

# To use with a Scrapy project:
# 1. Place this file in the spiders directory of your project
# 2. Run: scrapy crawl mega_spider -o data.csv


if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings

    # This allows you to run the file directly
    process = CrawlerProcess(get_project_settings())
    # Choose which spider to run
    process.crawl(MegaSpider)
    # process.crawl(ExampleEcommerceSiteSpider)
    # process.crawl(ExampleNewsSpider)
    process.start()
