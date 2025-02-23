# -*- coding: utf -8 -*- #
"""
@filename:login.py
@author:ChenWenGang
@time:2025-02-22
"""
# 接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递的，接口方法被调用时需要返回对应的响应结果

# 导包
import requests
import config


# 创建接口类
class LoginAPI:
    # 初始化方法
    def __init__(self):
        # 指定url基本信息
        # self.url_verify = "http://huike-crm.itheima.net/api/captchaImage"
        self.url_verify = config.BASE_URL + "/api/captchaImage"
        # self.url_login = "http://huike-crm.itheima.net/api/login"
        self.url_login = config.BASE_URL + "/api/login"

    # 验证码
    def get_verify_code(self):
        return requests.get(self.url_verify)

    # 登录
    def login(self, test_data):
        return requests.post(self.url_login, json=test_data)


if __name__ == "__main__":
    pass
