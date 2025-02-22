# -*- coding: utf -8 -*- #
"""
@filename:test07_select_course.py
@author:ChenWenGang
@time:2025-02-22
"""
# 导包
from api.login import LoginAPI
from api.course import CourseAPI


# 创建测试类
class TestSelectCourseAPI:
    # 类变量
    token = None

    # 前置处理
    @classmethod
    def setup_class(cls):
        # 初始化接口类
        cls.login_api = LoginAPI()
        cls.course_api = CourseAPI()
        # 获取验证码
        res_v = cls.login_api.get_verify_code()
        # 登录
        login_data = {
            "username": "admin",
            "password": "123456",
            "code": "2",
            "uuid": res_v.json()["uuid"],
        }
        res_l = cls.login_api.login(test_data=login_data)
        # 提取登录成功的token
        TestSelectCourseAPI.token = res_l.json()["token"]
        print(TestSelectCourseAPI.token)

    # 后置处理
    @classmethod
    def teardown_class(cls):
        pass

    # 测试用例1:查询存在的课程列表
    def test_select_course(self):
        test_data = {"name": "测试开发提升课01"}
        response = self.course_api.select_course(
            test_data=test_data, token=TestSelectCourseAPI.token
        )
        assert response.status_code == 200
        assert response.json()["code"] == 200
        assert "成功" in response.json()["msg"]

    # 测试用例2:查询失败，用户未登录
    def test_select_course_fail(self):
        test_data = {"subject": "6"}
        response = self.course_api.select_course(test_data=test_data, token="xxx")
        assert response.status_code == 200
        assert response.json()["code"] == 401
        assert "失败" in response.json()["msg"]


if __name__ == "__main__":
    pass
