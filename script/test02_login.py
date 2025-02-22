# -*- coding: utf -8 -*- #
"""
@filename:test02_login.py
@author:ChenWenGang
@time:2025-02-22
"""
# 需求：登录成功

# 导包
import requests

# 发送请求
url = "https://kdtx-test.itheima.net/api/login"
headers = {"Content-Type": "application/json"}
json = {
    "username": "admin",
    "password": "admin123",
    "code": 2,
    "uuid": "f70bcbc9d48d4898aa8379d5a65e0f20",
}
response = requests.post(url=url, headers=headers, json=json)

# 查看响应
print(response.status_code)
print(response.json())
if __name__ == "__main__":
    pass
