#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 基地址是本项目根目录
sys.path.append(BASE_DIR)
import datetime
from yxf_yixue.qimen import QimenApi
from yxf_yixue.wannianli import WannianliApi


if __name__ == '__main__':
    a = QimenApi()
    string = '1996/02/29 23:16'
    obj = datetime.datetime(2019, 3, 9, 12, 40)
    a.paipan(obj,bujufangfa='排宫')
    print(a.print_pan())
    pass