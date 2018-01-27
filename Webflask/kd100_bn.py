#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

# 3rd party API : KD100
# http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text= <EXP CODE>  [POST]
# http://www.kuaidi100.com/query?type= <COMPANY CODE> &postid= <EXP CODE>  [GET]

# POST : resp['auto'][0]['comCode']
# raise IndexError (None Array)

# GET: pkgresp['data'][0]['context']
# check if pkgresp['status'] == 200, else is error

# kd100_company.json http://www.kuaidi100.com/js/share/company.js

import requests, sys, json
from modules_logger import logger

sys.stdout = logger
sys.stderr = logger


def checkcmpy(expn):
    base = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text='
    query = str(expn)
    url = base + query
    req = requests.post(url=url)
    resp = req.json()
    try:
        company = resp['auto'][0]['comCode']
    except IndexError:
        return json.dumps({'status': 404, 'pkgid': query, 'bmsg': 'Package\'s Company cannot be detected.'})
    return company


def
