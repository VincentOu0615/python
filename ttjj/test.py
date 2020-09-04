#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import json


# (1)基金列表
# http://fund.eastmoney.com/js/fundcode_search.js
# 格式：["000001","HXCZ","华夏成长","混合型","HUAXIACHENGZHANG"]

# (2)基金净值数据
# http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=377240
# http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=160220&page=1
# http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=160220&page=1&per=50
# http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=377240&page=1&per=20&sdate=2017-03-01&edate=2017-03-01

# 格式：var apidata={ content:"<table class='w782 comm lsjz'><thead><tr><th class='first'>净值日期</th><th>单位净值</th><th>累计净值</th><th>日增长率</th><th>申购状态</th><th>赎回状态</th><th class='tor last'>分红送配</th></tr></thead><tbody><tr><td>2017-03-01</td><td class='tor bold'>2.1090</td><td class='tor bold'>2.1090</td><td class='tor bold red'>0.29%</td><td>开放申购</td><td>开放赎回</td><td class='red unbold'></td></tr></tbody></table>",records:1,pages:1,curpage:1};

url = ['http://fund.eastmoney.com/f10/F10DataApi.aspx']
stock_code = ['377240']

urltest = 'http://fund.eastmoney.com/js/fundcode_search.js'

df = pd.read_text(urltest)
#json_format = json.dumps(df)

print(df.to_string())
# print(type(json_format))
