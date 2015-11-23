# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request

import json
from mongo_data import commodity


update = Blueprint('update', __name__)


@update.route("/update/single", methods=["POST"])
def update_single():
    data = request.data.decode("utf-8")
    ret = dict()
    ret["err_no"] = 0
    ret["err_msg"] = "success"
    try:
        data = json.loads(data)
        comm = commodity.Commodity.objects(index=data['index']).first()
        if not comm:
            raise IndexError
        for upda in data['updates']:
            if upda == 'expect_price':
                comm.expect_price = data['updates']['expect_price']
            elif upda == 'name':
                comm.name = data['updates']['name']
            elif upda == 'source_id':
                comm.name = data['updates']['source_id']
            elif upda == 'price_list':
                comm.price_list = data['updates']['price_list']
            elif upda == 'description':
                comm.description = data['updates']['description']
            elif upda == 'img_file':
                comm.img_file = data['updates']['img_file']
            elif upda == 'commodity_url':
                comm.commodity_url = data['updates']['commodity_url']
            elif upda == 'commodity_source':
                comm.commodity_source = data['updates']['commodity_source']
        comm.save()
    except IndexError:
        ret["err_no"] = 1
        ret["err_msg"] = "can not find data"
        return jsonify(ret)
    except KeyError:
        ret["err_no"] = 1
        ret["err_msg"] = "your request is illegal or you have spelled the key wrong"
        return jsonify(ret)
    except ValueError:
        ret["err_no"] = 2
        ret["err_msg"] = "update error, check your update information"
        return jsonify(ret)
    return jsonify(ret)


@update.route("/update/multi", methods=["POST"])
def update_multi():
    datas = request.data.decode("utf-8")
    count = 0
    ret = dict()
    ret["err_no"] = 0
    ret["err_msg"] = "success update count:" + str(count)
    try:
        datas = json.loads(datas)
        for data in datas:
            comm = commodity.Commodity.objects(index=data['index']).first()
            if not comm:
                raise IndexError
            for upda in data['updates']:
                if upda == 'expect_price':
                    comm.expect_price = data['updates']['expect_price']
                elif upda == 'name':
                    comm.name = data['updates']['name']
                elif upda == 'source_id':
                    comm.name = data['updates']['source_id']
                elif upda == 'price_list':
                    comm.price_list = data['updates']['price_list']
                elif upda == 'description':
                    comm.description = data['updates']['description']
                elif upda == 'img_file':
                    comm.img_file = data['updates']['img_file']
                elif upda == 'commodity_url':
                    comm.commodity_url = data['updates']['commodity_url']
                elif upda == 'commodity_source':
                    comm.commodity_source = data['updates']['commodity_source']
            comm.save()
            count += 1
    except IndexError:
        ret["err_no"] = 1
        ret["err_msg"] = "can not find data, success update count:" + str(count)
        return jsonify(ret)
    except KeyError:
        ret["err_no"] = 2
        ret["err_msg"] = "the key wrong, success update count:" + str(count)
        return jsonify(ret)
    except ValueError:
        ret["err_no"] = 2
        ret["err_msg"] = "value error, success update count:" + str(count)
        return jsonify(ret)
    ret["err_msg"] = "success update count:" + str(count)
    return jsonify(ret)
