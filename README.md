# Actowiz Custom Proxy Middleware

Actowiz Custom Proxy Middleware is a Scrapy middleware that allows you to easily integrate custom proxies into your Scrapy projects.

## Installation

You can install the package using pip. Run the following command:

```bash
pip install git+https://github.com/Actowiz/Actowiz_Custom_Proxy.git
```
 In your Scrapy project, configure your proxy settings in the settings.py file.


```
# Set your proxy-related settings

PROXY_NAME = 'ACT_CUSTOM_PROXY_1'
PROXY_OPTIONS = {
   "key_id" : 1,
   "proxy_options" : {
            "custom_headers": 'false',
            "render": 'false',
            "country_code": "us",
   },
}
```

In your settings.py file, add the following configuration to enable the middleware:
```
# Enable Actowiz Custom Proxy Middleware

DOWNLOADER_MIDDLEWARES = {
    'actowiz_custom_proxy.middleware.ActowizProxyMiddleware': 350,
}
```

Adjust the priority (350 in this example) according to your project's requirements.

