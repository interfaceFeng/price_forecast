# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename

import json
import os
import config
from mongo_data import commodity
from mongoengine import *


upload = Blueprint('upload', __name__)


@upload.route("/upload/single", methods=["POST"])
def upload_single():
    data = request.data.decode("UTF-8")
    ret = dict()
    ret["err_no"] = 0
    ret["err_msg"] = "success"
    try:
        data = json.loads(data)
        index = data["commodity_source"] + data["source_id"]
        comm = commodity.Commodity()
        comm.name = data["name"]
        comm.description = data["description"]
        comm.index = index
        comm.price_list = data["price_list"]
        comm.expect_price = data["expect_price"]
        comm.source_id = data["source_id"]
        comm.commodity_source = data["commodity_source"]
        comm.commodity_url = data["commodity_url"]
        comm.save()
    except KeyError as e:
        ret["err_no"] = 1
        ret["err_msg"] = "not have key" + str(e)
    except ValueError:
        ret["err_no"] = 1
        ret["err_msg"] = "json data resolve failed"
    except NotUniqueError:
        ret["err_no"] = 2
        ret["err_msg"] = "you must not upload the same information twice"
    return jsonify(ret)


@upload.route("/upload/multi", methods=["POST"])
def upload_multi():
    count = 0
    datas = request.data.decode("utf-8")
    ret = dict()
    ret["err_no"] = 0
    ret["err_msg"] = "0"
    comms = []
    try:
        datas = json.loads(datas)
        for data in datas:
            index = data["commodity_source"] + data["source_id"]
            comm = commodity.Commodity()
            comm.name = data["name"]
            comm.description = data["description"]
            comm.price_list = data["price_list"]
            comm.index = index
            comm.expect_price = data["expect_price"]
            comm.source_id = data["source_id"]
            comm.commodity_source = data["commodity_source"]
            comm.commodity_url = data["commodity_url"]
            count += 1
            comms.append(comm)
        commodity.Commodity.objects.insert(doc_or_docs=comms)
    except KeyError as e:
        ret["err_no"] = 1
        ret["err_msg"] = "not have key" + str(e)
        return jsonify(ret)
    except ValueError:
        ret["err_no"] = 1
        ret["err_msg"] = "json data resolve failed"
        return jsonify(ret)
    except NotUniqueError as e:
        ret["err_no"] = 1
        ret["err_msg"] = "you must not upload the same information twice, " + str(e)
        return jsonify(ret)
    ret["err_msg"] = str(count)
    return jsonify(ret)


@upload.route("/upload/imgupload/<source_id>/<commodity_source>", methods=["POST"])
def imgupload(source_id, commodity_source):
    ret = dict()
    ret["err_no"] = 0
    ret["err_msg"] = "success"
    try:
        f = request.files['img_file']
        tmp = f.filename.split(".")
        tmp[0] = source_id
        f.filename = ".".join(tmp)
        print(f.filename)
        if not f:
            raise FileNotFoundError
        try:
            fname = secure_filename(f.filename)
            f.save(os.path.join(config.IMAGE_FOLDER, commodity_source, fname))
        except FileExistsError:
            ret["err_no"] = 1
            ret["err_msg"] = "save this image error"
            return jsonify(ret)
    except FileNotFoundError:
        ret["err_no"] = 1
        ret["err_msg"] = "not have this file or open file error"
        return jsonify(ret)

    return jsonify(ret)


