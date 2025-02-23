# -*- coding: utf -8 -*- #
"""
@filename:course.py
@author:ChenWenGang
@time:2025-02-22
"""
# 课程模块接口封装：核心在于依据接口文档实现接口信息的封装，重点关注接口如何被调用
# 导包
import requests
import config


# 创建接口类
class CourseAPI:
    # 初始化
    def __init__(self):
        # self.url_add_course = "http://huike-crm.itheima.net/api/clues/course"
        self.url_add_course = config.BASE_URL + "/api/clues/course"
        # self.url_select_course = "http://huike-crm.itheima.net/api/clues/course/list"
        self.url_select_course = config.BASE_URL + "/api/clues/course/list"

    # 课程添加接口
    def add_course(self, test_data, token):
        return requests.post(
            url=self.url_add_course, json=test_data, headers={"Authorization": token}
        )

    # 课程查询接口，直接用params参数传递查询条件
    def select_course(self, test_data, token):
        return requests.get(
            url=self.url_select_course,
            params=test_data,
            headers={"Authorization": token},
        )

    # 课程修改接口
    def update_course(self, test_data, token):
        return requests.put(
            url=self.url_add_course, json=test_data, headers={"Authorization": token}
        )

    # 课程删除接口
    def delete_course(self, test_data, token):
        return requests.delete(
            url=self.url_add_course + f"/{test_data}", headers={"Authorization": token}
        )


if __name__ == "__main__":
    pass
