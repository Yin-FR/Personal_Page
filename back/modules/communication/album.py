#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: album.py
# @Author: 檀寅
# @Time: 2020年08月27日11:35
# @说明: 

import pandas as pd
import json

def get_album_links(albumLink, number):
    number = int(number)
    albumLink = 'https://' + albumLink
    print(albumLink)
    link_csv = list(pd.read_csv(albumLink)['ref'])
    if number == 0 or number > len(link_csv):
        links = link_csv
    else:
        links = link_csv[:number]
    return json.dumps(links)