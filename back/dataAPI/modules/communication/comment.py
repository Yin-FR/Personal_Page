#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: comment.py
# @Author: 檀寅
# @Time: 2020年08月21日18:13
# @说明: 

import pymysql
import pandas as pd
import json
import time

account_info = pd.read_csv('accounts/accountMysql.csv')
[host, userN, password, database] = [account_info[each][0] for each in account_info.columns]

config = {
    "host": host,
    "user": userN,
    "password": password,
    "database": database
}


def comment_store(userName, message):
    time_now = time.gmtime()
    hour = time_now.tm_hour + 8
    if hour > 23:
        hour -= 24
    timeNow = str(time_now.tm_year) + '.' + str(time_now.tm_mon) + '.' + str(time_now.tm_mday) + '\n' + str(hour) \
              + ':' + str(time_now.tm_min) + ':' + str(time_now.tm_sec)

    db = pymysql.connect(**config)
    cursor = db.cursor()

    sql = "	INSERT INTO comments(user, content, time) VALUES('{}', '{}', '{}')".format(userName, message, timeNow)
    cursor.execute(sql)
    db.commit()


def comment_read():
    db = pymysql.connect(**config)
    cursor = db.cursor()

    sql = " SELECT * FROM comments ORDER BY id DESC"
    cursor.execute(sql)
    data = cursor.fetchall()

    result = []
    for each_commentObj in data:
        result.append({
            'timeSend': each_commentObj[3],
            'userNameSend': each_commentObj[1],
            'messageSend': each_commentObj[2]
        })

    resultSend = json.dumps(result)

    return resultSend
