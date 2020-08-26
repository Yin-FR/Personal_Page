#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: views.py
# @Author: 檀寅
# @Time: 2020年08月21日15:59
# @说明: 

from flask import Blueprint, request
from modules.communication.comment import comment_store, comment_read
import json

communication = Blueprint('communication', __name__)


@communication.route('/comments', methods=['POST', 'GET'])
def operationComment():
    if request.method == 'POST':
        dataGot = (request.get_data())
        data = json.loads(dataGot)
        print(data)
        print(type(data['user']))
        userName = data['user']
        content = data['comment']
        if userName and content:
            comment_store(userName, content)
        return 'upload succeed'
    if request.method == 'GET':
        return comment_read()

@communication.route('/test', methods=['GET'])
def test():
    if request.method == 'GET':
        return 'test succeed!'