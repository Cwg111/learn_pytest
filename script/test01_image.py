# -*- coding: utf -8 -*- #
"""
@filename:test01_image.py
@author:ChenWenGang
@time:2025-02-22
"""
# 获取图片验证码

# 导包
import requests

# 发送验证码
response = requests.get(url='https://kdtx-test.itheima.net/api/captchaImage')

# 查看响应
print(response.status_code)
print(response.text)
if __name__ == '__main__':
    pass
