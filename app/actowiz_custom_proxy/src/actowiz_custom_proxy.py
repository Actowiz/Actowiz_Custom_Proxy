from scrapy import signals
from elasticsearch import Elasticsearch
import os, socket


class ActowizProxyMiddleware:

    def __init__(self, settings):
        self.proxy_name = settings.get('PROXY_NAME')
        self.project_name = settings.get('BOT_NAME')
        self.proxy_options = settings.get('PROXY_OPTIONS')
        self.proxy = os.environ.get(f"{self.proxy_name}_{self.proxy_options.get('key_id')}")
        self.proxy_count = {}
        self.ipaddress = socket.gethostbyname(socket.gethostname())
        self.es = Elasticsearch(
            hosts="https://localhost:9200",
            api_key="NkdvQ3lZd0JiWDBsRWp1ckZDd1E6ZEktTHZ3QXNSdnEyX1FpaC1nWTRnQQ==",
            verify_certs=False
        )

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls(crawler.settings)
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        if self.proxy:
            if self.proxy_name == 'ACT_CUSTOM_PROXY_1':
                if self.proxy_options:
                    proxy = f"http://scraperapi.keep_headers={self.proxy_options.get('proxy_options').get('custom_headers')}.render={self.proxy_options.get('proxy_options').get('render')}.country_code={self.proxy_options.get('proxy_options').get('country_code')}:{self.proxy}@proxy-server.scraperapi.com:8001"
                else:
                    proxy = f"http://scraperapi:{self.proxy}@proxy-server.scraperapi.com:8001"
                request.meta['proxy'] = proxy

            print(f"Request was made with {self.proxy_name}")


    def process_response(self, request, response, spider):

        if response.status in [200, 404]:
            log_data = {
                'project_name': self.project_name,
                'proxy_name': self.proxy_name,
                'usage': 1,
                'ip': self.ipaddress,
                'domain': response.url.split('/')[2],
            }
            self.es.index(index='actowiz_proxy_logs', body=log_data)
            return response

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

    def spider_closed(self, spider):
        pass
