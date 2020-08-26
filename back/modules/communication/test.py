#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: test.py
# @Author: 檀寅
# @Time: 2020年08月21日19:17
# @说明: 

import pymysql
import pandas as pd
import json

account_info = pd.read_csv('../../accounts/accountMysql.csv')
[host, userN, password, database] = [account_info[each][0] for each in account_info.columns]

config = {
    "host": host,
    "user": userN,
    "password": password,
    "database": database
}

if __name__ == "__main__":
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
    print(resultSend)