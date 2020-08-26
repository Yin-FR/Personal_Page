#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: views.py
# @Author: 檀寅
# @Time: 2020年08月24日17:37
# @说明: 

from flask import Blueprint, request
from modules.ML.datasets.return_datasets import return_datasets, return_dataset_by_item

datasets = Blueprint('datasets',__name__)

@datasets.route('/', methods=['GET'])
def get_data():
    if request.method == 'GET':
        dataName = request.args.get('dataName')
        dataType = request.args.get('dataType')
        return return_datasets(dataset_name=dataName, typeData=dataType)

@datasets.route('/byItem', methods=['GET'])
def get_data_by_item():
    if request.method == 'GET':
        dataName = request.args.get('dataName')
        dataType = request.args.get('dataType')
        item = request.args.get('item')
        return return_dataset_by_item(dataName, dataType, item)