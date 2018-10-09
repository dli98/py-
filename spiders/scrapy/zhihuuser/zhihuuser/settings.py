# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # 'cookie': '_zap=f37d31e4-80f2-4d15-b979-c7fc3abf523b; __DAYU_PP=ZrZzUamqaF2yI7BvJy7mffffffff87568b7d0fd3; d_c0="AMBuJn8MjA2PTmFSWUEogiSXV4Zdowy3dfM=|1525516816"; _xsrf=i6Qjl4HlM4ZTtXxId0AEVVol4qscjJ4o; q_c1=e497e14221ae4a2cb07578849ceabb8e|1534311582000|1522547411000; l_cap_id="MzU2ZjQxNWI4NTA3NDdjOTgxZWQ5ZjZkOGUwMTkxNzY=|1534908529|82317c3ea318848bbdcaff2b778a00be33f318d8"; r_cap_id="M2U5MjIyZDYyMDQwNDNhMGExODA0MTRlYWQ0MDBhYmQ=|1534908529|62264764d20e3abdb295cbd6893c7515d224fe8d"; cap_id="ZjMxYzA3ZWYyZjQxNDRjNmE0ZDRjYzAwZmEwYWIxZGY=|1534908529|299655baea2844e271b43ecd16df1fa0490708f5"; capsion_ticket="2|1:0|10:1534923613|14:capsion_ticket|44:ZjI1ZDRiNzBiMjY5NGM5NTgyNGE4YjM2NWE1NWE1MzI=|0f245d3e1de8d2660a8f7cb353a23120c1fa2055940e1c1ddd34f8382e6875bd"; z_c0="2|1:0|10:1534923668|4:z_c0|92:Mi4xLXNIQUN3QUFBQUFBd0c0bWZ3eU1EU1lBQUFCZ0FsVk5sR0ZxWEFENVV4c2dSZ25ZeTVNbThrTF9wU3E2SE9NdUx3|91de78a7387d99dea89661378cd4bc952af98b159396b47ffee1d7af26e1ddc7"; __utma=155987696.2038777987.1534907047.1534907047.1535282905.2; __utmc=155987696; __utmz=155987696.1534907047.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/35682031; tgw_l7_route=c919f0a0115842464094a26115457122',
    # 'referer': 'https://www.zhihu.com/people/excited-vczh/following?page=4',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuuser.pipelines.MongoPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

MONGO_URL = 'localhost'
MONGO_DB = 'zhihuuser'

REDIS_URL = 'redis://linux:@192.168.70.131:6379'
