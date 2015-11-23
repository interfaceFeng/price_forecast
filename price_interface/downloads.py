# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename

import json
import os
import config
from mongo_data import commodity


download = Blueprint('download', __name__)


@download.route("/download/single", methods=["Post"])
def single_download():
    data = request.data.decode("utf-8")
    ret = dict()
    try:
        data = json.loads(data)
        comm = commodity.Commodity.objects(index=data['index']).first()
        ret["name"] = comm.name
        ret["index"] = comm.index
        ret["price_list"] = comm.price_list
        ret["description"] = comm.description
        ret["expect_price"] = comm.expect_price
        ret["source_id"] = comm.source_id
        ret["img_file"] = comm.img_file
        ret["commodity_url"] = comm.commodity_url
        ret["commodity_source"] = comm.commodity_source
    except:
        ret = dict()
        ret["err_msg"] = "can not find data or data is damaged"

    return jsonify(ret)

