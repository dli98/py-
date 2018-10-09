

from scrapy import cmdline
name = 'quotes'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())