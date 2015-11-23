# -*- coding: utf-8 -*-

from mongoengine import *

source_list = ["jd"]


class Commodity(Document):
    price_list = DictField()
    name = StringField(max_length=100)
    index = StringField(max_length=300, unique=True)
    description = StringField(max_length=300)
    expect_price = IntField()
    source_id = StringField(max_length=50)
    img_file = StringField(max_length=100)
    commodity_url = StringField(max_length=300)
    commodity_source = StringField(choices=source_list)
    meta = {
        'indexes': ['index']
    }

