#!/usr/bin/env python
# -* coding:utf-8 -*
import json
import re
import time
import logging
from elasticsearch import Elasticsearch
import traceback
from manage import main
from pub import time_common
import datetime

logger = logging.getLogger("info.logger")

ES_TIME_OUT = 25
MAX_RETRIES = 2
YZF_ES_USER = 'elastic'
YZF_ES_PWD = 'Log2021@es'
YZF_IPS = ["11.177.107.65:9200"]
APP_DEPARTMENT = 'smart_log-%s'  # 索引案例：smart_log-2021.10.09
DEPARTMENT_TYPE = '_doc'


def get_es(user=YZF_ES_USER):
    es_conn = None
    try:
        if user:
            es_conn = Elasticsearch(YZF_IPS, timeout=ES_TIME_OUT, max_retries=MAX_RETRIES, http_auth=(user, YZF_ES_PWD),
                                    retry_on_timeout=True)
        else:
            es_conn = Elasticsearch(YZF_IPS, timeout=ES_TIME_OUT, max_retries=MAX_RETRIES, retry_on_timeout=True)
    except Exception as e:
        pass
    return es_conn


es_conn = get_es()


def parse_source(response, funcDesc=None):
    '''格式化返回结果
    :return:list
    '''
    return_list = []
    try:
        for hit in response['hits']['hits']:
            return_list.append(hit['_source'])
        if len(return_list) == 0 and funcDesc:
            warn_info = "ES业务模块【%s】数据返回为空" % (funcDesc)
            logger.info(warn_info)
    except Exception as e:
        # 告警
        return return_list
    return return_list


def es_search(body, time_range=[], other_index=None):
    """es查询"""
    response = {}
    index_name = []
    # print("body:",body)
    try:
        if body is None:
            return {}

        if other_index is not None:  # 为空则默认查询当天
            index_name = other_index

        elif len(time_range) == 2:  # 查询范围内
            index_list = []
            date_list = time_common.get_time_range("day", time_range)
            for item in date_list:
                if es_conn.indices.exists(APP_DEPARTMENT % (str(item["data_time"]).replace("-", "."))):
                    index_list.append(APP_DEPARTMENT % (str(item["data_time"]).replace("-", ".")))
            index_name = index_list

        else:
            # index_name = APP_DEPARTMENT%(time_common.nowTime(4,"%Y.%m.%d"))
            index_name = get_effective_index()
            # print(index_name)

        if index_name:
            response = es_conn.search(index=index_name, body=body)
            response["index_name"] = index_name
        else:
            response["index_name"] = index_name
            return response
    except Exception as e:
        print("es_search traceback:%s" % (traceback.format_exc()))
        logger.info("es_search traceback:%s" % (traceback.format_exc()))

    # print("结果：", response)
    return response


def get_aggr(data={}):
    """
    获取聚合结果
    """
    # return data["aggregations"]['Command']['buckets']
    return data.setdefault("aggregations", {}).setdefault('Command', {}).setdefault('buckets', {})


def get_effective_index():
    APP_DEPARTMENT = 'smart_log-%s'
    now_day = datetime.datetime.today().strftime('%Y-%m-%d')
    es_conn = get_es()
    start_day = datetime.datetime.today() + datetime.timedelta(-4)
    start_day = start_day.strftime('%Y-%m-%d')
    index_list = []
    date_list = time_common.get_time_range("day", [start_day, now_day])
    for item in date_list:
        if es_conn.indices.exists(APP_DEPARTMENT % (str(item["data_time"]).replace("-", "."))):
            index_list.append(APP_DEPARTMENT % (str(item["data_time"]).replace("-", ".")))

    return index_list[-1]
