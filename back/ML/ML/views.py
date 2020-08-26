#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: views.py
# @Author: 檀寅
# @Time: 2020年08月26日11:33
# @说明: 

from flask import Blueprint, request
from modules.ML.titanic.titanic_ML import titanic_use_model

ML = Blueprint('ML', __name__)

@ML.route('/titanic', methods=['GET'])
def return_titanic_result():
    if request.method == 'GET':
        items = request.args.get('items')
        modelName = request.args.get('modelName')
        return titanic_use_model(itemSelected=items, modelName=modelName)