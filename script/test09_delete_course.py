# -*- coding: utf -8 -*- #
"""
@filename:test09_delete_course.py
@author:ChenWenGang
@time:2025-02-22
"""
# 导包
from api.login import LoginAPI
from api.course import CourseAPI


# 创建测试类，这里待修改，因为可以通过参数化来实现，简化代码!!!!!!!!!!!!!
class TestDeleteCourseAPI:
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
        TestDeleteCourseAPI.token = res_l.json()["token"]
        print(TestDeleteCourseAPI.token)

    # 后置处理
    @classmethod
    def teardown_class(cls):
        pass

    # 测试用例1：课程删除成功
    def test_delete_course_success(self):
        response = self.course_api.delete_course(
            test_data=110, token=TestDeleteCourseAPI.token
        )
        assert response.status_code == 200
        assert response.json()["code"] == 200
        assert "成功" in response.json()["msg"]

    # 测试用例2：课程删除失败(id不存在)
    def test_delete_course_failed_id_not_exist(self):
        response = self.course_api.delete_course(
            test_data=1, token=TestDeleteCourseAPI.token
        )
        assert response.status_code == 200
        assert response.json()["code"] == 500
        assert "失败" in response.json()["msg"]

    # 测试用例3：课程添加失败(未登录)
    def test_add_course_failed(self):
        response = self.course_api.add_course(test_data=111, token="xxx")
        assert response.status_code == 200
        assert response.json()["code"] == 401
        assert "失败" in response.json()["msg"]


if __name__ == "__main__":
    pass
