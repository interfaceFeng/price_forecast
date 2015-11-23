# -*- coding: utf-8 -*-
from flask import request;
import os
import json, config

data2 = '[{"name": "aaa", "description": "xxx", "price_list": {"2015-3-10": 300}, "expect_price": 300, ' \
        '"source_id": "3", "index": "jd3"' \
        '"commodity_url": "xxx", "commodity_source": "jd"},'\
        '{"name": "bbb", "description": "xxx", "price_list": {"2015-3-10": 300}, "expect_price": 300, ' \
        '"source_id": "4", "index": "jd4"' \
        '"commodity_url": "xxx", "commodity_source": "jd"},'\
        '{"name": "ccc", "description": "xxx", "price_list": {"2015-3-10": 300}, "expect_price": 300, ' \
        '"source_id": "5", "index": "jd5"' \
        '"commodity_url": "xxx", "commodity_source": "jd"}]'

data = json.dumps(data2)

print(data)

