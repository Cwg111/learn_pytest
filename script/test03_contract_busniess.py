# -*- coding: utf -8 -*- #
"""
@filename:test03_contract_busniess.py
@author:ChenWenGang
@time:2025-02-22
"""
# 导包
from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI

# import pytest


# 创建测试类
class TestContractBusiness:
    # 初始化
    token = None

    # 前置处理
    def setup_class(self):
        # 实例化登录API
        self.login_api = LoginAPI()
        # 实例化课程API
        self.course_api = CourseAPI()
        # 实例化合同API
        self.contract_api = ContractAPI()
        # print("前置处理")

    # 后置处理
    def teardown_class(self):
        pass

    # 测试用例1:登录成功
    def test01_login_success(self):
        # self.login_api = LoginAPI()
        # 获取验证码
        verify_code = self.login_api.get_verify_code()
        print(verify_code.status_code)
        print(verify_code.json())
        # 打印uuid数据
        print(verify_code.json()["uuid"])

        # 登录
        res_l = self.login_api.login(
            test_data={
                "username": "demo",
                "password": "015itheima.CN032@.20250222",
                "code": "2",
                "uuid": verify_code.json()["uuid"],
            }
        )
        print(res_l.status_code)
        print(res_l.json())
        # 提取登录成功之后的token数据并保存在类的属性中，注意必须要登录成功之后才能获取到token数据，现在登录不了的
        TestContractBusiness.token = res_l.json()["token"]
        print(TestContractBusiness.token)

    # 测试用例2:添加课程成功
    def test02_add_course_success(self):
        add_course_data = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01的介绍",
        }
        response = self.course_api.add_course(
            test_data=add_course_data, token=TestContractBusiness.token
        )
        print(response.json())

    # 测试用例3:上传合同成功
    def test03_upload_contract_success(self):
        f = open("../data/test.pdf", "rb")
        response = self.contract_api.upload_contract(
            test_data=f, token=TestContractBusiness.token
        )
        print(response.json())
        f.close()

    # 测试用例4:添加合同成功
    def test04_add_contract_success(self):
        # 要保证合同号是唯一的
        add_contract_data = {
            "name": "测试8888",
            "phone": "13612345678",
            "contractNo": "HT10012003",
            "subject": "6",
            "courseId": "99",
            "channel": "0",
            "activityId": "77",
            "filename": "xxx",
        }
        response = self.contract_api.add_contract(
            test_data=add_contract_data, token=TestContractBusiness.token
        )
        print(response.json())


if __name__ == "__main__":
    pass
