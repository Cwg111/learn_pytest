# -*- coding: utf -8 -*- #
"""
@filename:contract.py
@author:ChenWenGang
@time:2025-02-22
"""
# 导包
import requests
import config


# 创建接口类
class ContractAPI:
    # 初始化
    def __init__(self):
        # self.url_upload = "http://huike-crm.itheima.net/api/common/upload"
        self.url_upload = config.BASE_URL + "/api/common/upload"
        # self.add_contract_url = "http://huike-crm.itheima.net/api/contract"
        self.add_contract_url = config.BASE_URL + "/api/contract"

    # 合同上传接口
    def upload_contract(self, test_data, token):
        return requests.post(
            self.url_upload, files={"file": test_data}, headers={"Authorization": token}
        )

    # 新增合同接口
    def add_contract(self, test_data, token):
        return requests.post(
            self.add_contract_url, json=test_data, headers={"Authorization": token}
        )


if __name__ == "__main__":
    pass
