# # Scrapy settings for medex project

# BOT_NAME = "medex"

# SPIDER_MODULES = ["medex.spiders"]
# NEWSPIDER_MODULE = "medex.spiders"

# # Crawl responsibly by identifying yourself with a realistic user agent
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"

# # Consider respecting robots.txt for ethical scraping
# ROBOTSTXT_OBEY = True

# # Reduce concurrent requests to avoid overwhelming the server
# CONCURRENT_REQUESTS = 4
# CONCURRENT_REQUESTS_PER_DOMAIN = 4
# CONCURRENT_REQUESTS_PER_IP = 4

# # Add a reasonable download delay to appear more human-like
# DOWNLOAD_DELAY = 3
# RANDOMIZE_DOWNLOAD_DELAY = True

# # Disable cookies to appear less like a tracking browser session
# COOKIES_ENABLED = False

# # Use HTTP caching to avoid re-downloading pages
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 86400  # Cache for 24 hours
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = [503, 504, 505, 500, 400, 401, 402, 403, 404]
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# # Enable AutoThrottle extension for intelligent rate limiting
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False

# # Add retry middleware to handle temporary failures
# RETRY_ENABLED = True
# RETRY_TIMES = 3
# RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]
# RETRY_PRIORITY_ADJUST = -1

# # Add realistic browser headers
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Connection": "keep-alive",
#     "Upgrade-Insecure-Requests": "1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Cache-Control": "max-age=0",
# }

# # Add rotating user agents middleware
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     'medex.middlewares.RotateUserAgentMiddleware': 120,
# }

# # Export settings
# FEED_EXPORT_ENCODING = "utf-8"
# FEED_FORMAT = "csv"
# FEED_URI = "medex_data.csv"

# # Resume crawling capability - helps with large crawls that might get interrupted
# JOBDIR = "crawls/medex-job"

# # Depth configuration - if you need to limit crawl depth
# DEPTH_LIMIT = 5  # Adjust as needed
# DEPTH_PRIORITY = 1
# DEPTH_STATS_VERBOSE = True

# # Timeout settings to handle slow responses
# DOWNLOAD_TIMEOUT = 180  # 3 minutes

# # Log level
# LOG_LEVEL = 'INFO'

# # Enable memory usage extension to monitor RAM usage
# EXTENSIONS = {
#     'scrapy.extensions.memusage.MemoryUsage': 0,
#     'scrapy.extensions.logstats.LogStats': 0,
# }
# MEMUSAGE_LIMIT_MB = 2048  # Limit memory usage to 2GB
# MEMUSAGE_NOTIFY_MAIL = ['youremail@example.com']  # Optional notification

# # Enable closespider extension to automatically stop after certain limits
# CLOSESPIDER_PAGECOUNT = 1000  # Stop after ~800 pages (with some buffer)
# CLOSESPIDER_TIMEOUT = 43200  # Stop after 12 hours


# Scrapy settings for medex project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "medex"

SPIDER_MODULES = ["medex.spiders"]
NEWSPIDER_MODULE = "medex.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "medex (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "medex.middlewares.MedexSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "medex.middlewares.MedexDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "medex.pipelines.MedexPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
DOWNLOAD_DELAY = 3
AUTOTHROTTLE_ENABLED = True
FEED_EXPORT_ENCODING = "utf-8"
FEED_FORMAT = "csv"
FEED_URI = "medex_data.csv"

CLOSESPIDER_PAGECOUNT = 5
