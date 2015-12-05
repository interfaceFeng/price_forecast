# -*- coding: utf-8 -*-
import requests
import config
import json

data1 = '{"name": "xxx", "description": "xxx", "price_list": {"2015-3-10": 300}, "expect_price": 300, ' \
        '"source_id": "2", ' \
        '"commodity_url": "xxx", "commodity_source": "jd"}'

data2 = '[{"name": "aaa", "description": "xxx", "price_list": {"2015-3-10": 300}, "expect_price": 300, ' \
        '"source_id": "9", ' \
        '"commodity_url": "xxx", "commodity_source": "jd"},'\
        '{"name": "bbb", "description": "xxx", "price_list": {"2015-3-10": 300}, "expect_price": 300, ' \
        '"source_id": "4", ' \
        '"commodity_url": "xxx", "commodity_source": "jd"},'\
        '{"name": "ccc", "description": "xxx", "price_list": {"2015-3-10": 300}, "expect_price": 300, ' \
        '"source_id": "5", ' \
        '"commodity_url": "xxx", "commodity_source": "jd"}]'
data_update = '{"source_id": "2", "commodity_source": "jd", "updates": {"expect_price": 1000, '\
              '"description": "cool", "price_list": {"2015-3-1": 800}, "commodity_url": "456", '\
              '"name": "wind"}}'

data_updates = '[{"source_id": "3", "commodity_source": "jd", "updates": {"expect_price": 1000, '\
                '"description": "cool", "price_list": {"2015-3-1": 800}, "commodity_url": "456", '\
                '"name": "wind"}}, ' \
                '{"source_id": "4", "commodity_source": "jd", "updates": {"expect_price": 900, '\
                '"description": "fail", "price_list": {"2015-2-1": 600}, "commodity_url": "hhh", '\
                '"name": "leaf"}}, ' \
                '{"source_id": "5", "commodity_source": "jd", "updates": {"expect_price": 100, '\
                '"description": "success", "price_list": {"2015-8-1": 200}, "commodity_url": "4aaa", '\
                '"name": "flower"}}, ' \
                '{"source_id": "2", "commodity_source": "tb", "updates": {"expect_price": 1000, '\
                '"description": "cool", "price_list": {"2015-3-1": 800}, "commodity_url": "456", '\
                '"name": "wind"}}]'
data_download = '{"commodity_source": "jd", "source_id": "2"}'
# files = {'img_file': open(config.IMAGE_PATH, 'rb')}
# print(files)
# ret = requests.request("POST", "http://127.0.0.1:5000/upload/single", data=data1)
# ret2 = requests.request("POST", "http://127.0.0.1:5000/upload/multi", data=data2)
# ret3 = requests.request("POST", "http://127.0.0.1:5000/upload/imgupload/2/jd", files=files)
# ret4 = requests.request("POST", "http://127.0.0.1:5000/update/single", data=data_update)
# ret5 = requests.request("POST", "http://127.0.0.1:5000/update/multi", data=data_updates)
ret6 = requests.request("POST", "http://127.0.0.1:5000/download/single", data=data_download)
# print(ret.content)
# print(ret2.content)
# print(ret3.content)
# print(ret4.content)
# print(ret5.content)
print(ret6.content)
