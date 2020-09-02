# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 11:00
# @Author  : felix
# @Email   : 876569085@qq.com
# @File    : demo.py
# @Software: PyCharm


import requests
import jsonpath
from common.handleconfig import conf

def recommend():
        """推荐模块"""
        url = "http://192.168.1.113:8060/api/community/video-blog/recommend"

        headers = {'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4NTI4OTYwMCIsIm1vYmlsZSI6IjEzMzg1Mjg5NjAwIiwiZXhwIjoxNTg1Mzg4MDMzLCJpYXQiOjE1ODUzMDE2MzMsIm1lbWJlcklkIjo0fQ.-xovrXk1CIy65BysmF-4m97FTwaxsR_ke3uyZ25gxMSKDQYp18xliqaAX4lS9mrjWl1nglxMvucePSuqffJBbg', 'Content-Type': 'application/json'}

        data = {
                    "current": "1",
                    "currentMemberId": "56",
                    "size": "30"
        }

        response = requests.post(url=url,headers=headers,json=data)

        res = response.json()
        rest = jsonpath.jsonpath(res,"$...id")
        test =list(set(rest))
        print(res)

def preview():
        """vlog详情模块"""
        url = "http://192.168.1.113:8060/api/community/video-blog/detail"

        headers = {'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4NTI4OTYwMCIsIm1vYmlsZSI6IjEzMzg1Mjg5NjAwIiwiZXhwIjoxNTg1Mzg4MDMzLCJpYXQiOjE1ODUzMDE2MzMsIm1lbWJlcklkIjo0fQ.-xovrXk1CIy65BysmF-4m97FTwaxsR_ke3uyZ25gxMSKDQYp18xliqaAX4lS9mrjWl1nglxMvucePSuqffJBbg', 'Content-Type': 'application/json'}
        data = {
                    "currentMemberId": "56",
                    "id": "2064"
                }

        response = requests.post(url=url,headers=headers,json=data)

        res = response.json()
        print(res)

# preview()
recommend()
