# -*- coding: utf -8 -*- #
"""
@filename:config.py
@author:ChenWenGang
@time:2025-02-21
"""
# 存放被测试项目基本信息，如url
# 导包
import os

# 设置项目环境域名
BASE_URL = "http://huike-crm.itheima.net"

# 获取项目根目录
BASE_PATH = os.path.dirname(__file__)
print(BASE_PATH)
if __name__ == "__main__":
    with open(BASE_PATH + "/data/login.json", "r", encoding="utf-8") as f:
        data = f.read()
        print(data)
