

from scrapy import cmdline
name = 'stocks'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())