# -*- coding: utf -8 -*- #
"""
@filename:test04_login.py
@author:ChenWenGang
@time:2025-02-22
"""
# 导包
from api.login import LoginAPI
import pytest
import json


# test_data = [
#     ("manager", "123456", 200, "成功", 200),
#     ("", "123456", 200, "错误", 500),
#     ("jack666", "123456", 200, "错误", 500),
# ]
# 读取json文件
def build_test_data(json_file):
    # 定义一个空列表
    test_data = []
    # 打开json文件
    with open(json_file, "r", encoding="utf-8") as f:
        # 加载json文件内容
        data = json.load(f)
        # 循环遍历测试数据
        for item in data:
            # 转换数据格式[{},{},{}]-->[(),(),()]
            test_data.append(
                (
                    item["username"],
                    item["password"],
                    item["status"],
                    item["message"],
                    item["code"],
                )
            )
    # 返回测试数据列表
    return test_data


# 创建测试类
class TestLoginAPI:
    # 初始化
    uuid = None

    # 前置处理
    @classmethod
    def setup_class(cls):
        # 实例化接口类
        cls.login_api = LoginAPI()
        # 获取验证码
        response = cls.login_api.get_verify_code()
        print(response.json())
        TestLoginAPI.uuid = response.json()["uuid"]
        print(TestLoginAPI.uuid)

    # 后置处理
    @classmethod
    def teardown_class(cls):
        pass

    # 登录成功,使用参数化测试
    @pytest.mark.parametrize(
        "username,password,code,msg,status_code", build_test_data("../data/login.json")
    )
    def test01_login(self, username, password, code, msg, status_code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLoginAPI.uuid,
        }
        response = self.login_api.login(login_data)
        # 断言响应状态码为200
        assert response.status_code == code

        # 断言响应数据包括'成功'或'错误'
        assert msg in response.text
        # 断言响应json数据中code值
        assert response.json()["code"] == status_code


if __name__ == "__main__":
    pass
