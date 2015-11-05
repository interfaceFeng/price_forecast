import requests

data = '{"name": "xxx, "description": "xxx", "price_list": {"2015-3-10": 300}, "expect_price": 300, ' \
       '"source_id": "2",' \
       '"commodity_url": "xxx", "commodity_source": "jd"}'
ret = requests.request("POST", "http://127.0.0.1:5000/upload/single", data=data)
print(ret.content)
