#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: manager.py
# @Author: 檀寅
# @Time: 2020年08月21日16:42
# @说明: 

from flask_script import Manager
from app import app1

if __name__ == "__main__":
    server = Manager(app1)
    server.run()