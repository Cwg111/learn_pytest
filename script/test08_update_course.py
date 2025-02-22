# -*- coding: utf -8 -*- #
"""
@filename:test08_update_course.py
@author:ChenWenGang
@time:2025-02-22
"""
# 导包
from api.login import LoginAPI
from api.course import CourseAPI


# 创建测试类
class TestUpdateCourseAPI:
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
        TestUpdateCourseAPI.token = res_l.json()["token"]
        print(TestUpdateCourseAPI.token)

    # 后置处理
    @classmethod
    def teardown_class(cls):
        pass

    # 测试用例1：课程修改成功
    def test_update_course_success(self):
        update_course_data = {
            "id": 93,
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01的介绍信息",
        }
        response = self.course_api.update_course(
            test_data=update_course_data, token=TestUpdateCourseAPI.token
        )
        assert response.status_code == 200
        assert response.json()["code"] == 200
        assert "成功" in response.json()["msg"]

    # 测试用例2：课程修改失败(未登录)
    def test_update_course_failed(self):
        update_course_data = {
            "id": 93,
            "name": "测试开发提升课02",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课02的介绍信息",
        }
        response = self.course_api.add_course(test_data=update_course_data, token="xxx")
        assert response.status_code == 200
        assert response.json()["code"] == 401
        assert "失败" in response.json()["msg"]


if __name__ == "__main__":
    pass
