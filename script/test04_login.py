# -*- coding: utf -8 -*- #
"""
@filename:test04_login.py
@author:ChenWenGang
@time:2025-02-22
"""
# 导包
from api.login import LoginAPI


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

    # 登录成功
    def test01_login_success(self):
        login_data = {
            "username": "admin",
            "password": "123456",
            "code": "2",
            "uuid": TestLoginAPI.uuid,
        }
        response = self.login_api.login(login_data)
        # 断言响应状态码为200
        assert response.status_code == 200

        # 断言响应数据包括'成功'
        assert "成功" in response.text
        # 断言响应json数据中code值
        assert response.json()["code"] == 200

    # 登录失败（用户名为空）
    def test02_without_username(self):
        login_data = {
            "username": "",
            "password": "123456",
            "code": "2",
            "uuid": TestLoginAPI.uuid,
        }
        response = self.login_api.login(login_data)
        # 断言响应状态码为200
        assert response.status_code == 200

        # 断言响应数据包括'错误'
        assert "错误" in response.text
        # 断言响应json数据中code值
        assert response.json()["code"] == 500

    # 登录失败（未注册用户）
    def test03_user_not_exist(self):
        login_data = {
            "username": "admin",
            "password": "123456",
            "code": "2",
            "uuid": TestLoginAPI.uuid,
        }
        response = self.login_api.login(login_data)
        # 断言响应状态码为200
        assert response.status_code == 200

        # 断言响应数据包括'错误'
        assert "错误" in response.text
        # 断言响应json数据中code值
        assert response.json()["code"] == 500


if __name__ == "__main__":
    pass
