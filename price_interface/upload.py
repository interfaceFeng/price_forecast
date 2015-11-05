from flask import request, Blueprint, jsonify

import json
import traceback
import mongo_data.commodity as commodity

__author__ = 'saber'


upload = Blueprint('upload', __name__)


@upload.route("/upload/single", methods=["POST"])
def upload_single():
    data = request.data.decode("UTF-8")
    ret = dict()
    ret["err_no"] = 0
    ret["err_msg"] = "success"
    try:
        data = json.loads(data)
        comm = commodity.Commodity()
        comm.name = data["name"]
        comm.description = data["description"]
        comm.price_list = data["price_list"]
        comm.expect_price = data["expect_price"]
        comm.source_id = data["source_id"]
        comm.commodity_source = data["commodity_source"]
        comm.commodity_url = data["commodity_url"]
        comm.save()
    except KeyError as e:
        ret["err_no"] = 1
        ret["err_msg"] = "not have key:" + str(e)
    except ValueError:
        ret["err_no"] = 2
        ret["err_msg"] = "json data resolve failed"
    return jsonify(ret)


@upload.route("/")
def index():
    return "Hello"
