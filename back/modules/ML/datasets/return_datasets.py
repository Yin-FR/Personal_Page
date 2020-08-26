#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: return_datasets.py
# @Author: 檀寅
# @Time: 2020年08月24日17:26
# @说明: 
import pandas as pd
import numpy as np
import os
import json

def return_datasets(dataset_name, typeData):
    dataset_location = os.path.join('modules/ML/datasets',dataset_name)
    dataset = pd.read_csv(os.path.join(dataset_location, '{}.csv'.format(typeData)))
    result = []
    for index, row in dataset.iterrows():
        rows = dict(row)
        for each in rows:
            if isinstance(rows[each], float):
                if np.isnan(rows[each]):
                    rows[each] = None
        result.append(rows)
    result_json = json.dumps(result)

    return result_json

def return_dataset_by_item(dataset_name, typeData, item):

    res = {}

    res['item'] = item

    if item == 'name':
        dataset_location = os.path.join('modules/ML/datasets', dataset_name)
        dataset = pd.read_csv(os.path.join(dataset_location, '{}.csv'.format(typeData)))
        result = list(dataset.columns)
        return json.dumps(result)

    else:
        dataset_origin = json.loads(return_datasets(dataset_name, typeData))
        items = [item, "Survived"]
        dataset_new = []
        for each_data in dataset_origin:
            data_to_be_append = []
            for each_item in items:
                data_to_be_append.append(each_data[each_item])
            dataset_new.append(data_to_be_append)

        survived = []
        not_survived = []
        for each_data in dataset_new:
            if each_data[1] == 1:
                survived.append(each_data)
            else:
                not_survived.append(each_data)

        print(survived)

        if item == 'Age':
            for each_data in survived:
                if each_data[0] is None:
                    each_data[0] = 'unKnown'
                else:
                    if each_data[0] < 16.0:
                        each_data[0] = '< 16'
                    elif 55.0 >= each_data[0] >= 16.0:
                        each_data[0] = '16 - 55'
                    else:
                        each_data[0] = '> 55'
            for each_data in not_survived:
                if each_data[0] is None:
                    each_data[0] = 'unKnown'
                else:
                    if each_data[0] < 16.0:
                        each_data[0] = '< 16'
                    elif 55.0 >= each_data[0] >= 16.0:
                        each_data[0] = '16 - 55'
                    else:
                        each_data[0] = '> 55'

        if item == 'Fare':
            for each_data in survived:
                if each_data[0] < 10:
                    each_data[0] = '< 10'
                elif 10 <= each_data[0] < 20:
                    each_data[0] = '10 - 20'
                elif 20 <= each_data[0] <30:
                    each_data[0] = '20 - 30'
                else:
                    each_data[0] = '> 30'
            for each_data in not_survived:
                if each_data[0] < 10:
                    each_data[0] = '< 10'
                elif 10 <= each_data[0] < 20:
                    each_data[0] = '10 - 20'
                elif 20 <= each_data[0] <30:
                    each_data[0] = '20 - 30'
                else:
                    each_data[0] = '> 30'

        res['survived'] = {}
        res['survived']['details'] = {}
        for each_data in survived:
            if each_data[0] not in res['survived']['details']:
                res['survived']['details'][each_data[0]] = 1
            else:
                res['survived']['details'][each_data[0]] += 1
        res['survived']['kinds'] = len(res['survived']['details'])

        res['notSurvived'] = {}
        res['notSurvived']['details'] = {}
        for each_data in not_survived:
            if each_data[0] not in res['notSurvived']['details']:
                res['notSurvived']['details'][each_data[0]] = 1
            else:
                res['notSurvived']['details'][each_data[0]] += 1
        res['notSurvived']['kinds'] = len(res['notSurvived']['details'])

        return json.dumps(res)