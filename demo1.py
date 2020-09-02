# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : demo1.py
# @Time     : 2020/4/1 16:21




import requests
import jsonpath
from common.handleconfig import conf

def createGoods():
        """新增商品"""

        url = "http://192.168.1.113:8060/api/community/video-blog/recommend"

        headers = {'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzM4NTI4OTYwMCIsIm1vYmlsZSI6IjEzMzg1Mjg5NjAwIiwiZXhwIjoxNTg1Mzg4MDMzLCJpYXQiOjE1ODUzMDE2MzMsIm1lbWJlcklkIjo0fQ.-xovrXk1CIy65BysmF-4m97FTwaxsR_ke3uyZ25gxMSKDQYp18xliqaAX4lS9mrjWl1nglxMvucePSuqffJBbg', 'Content-Type': 'application/json'}

        # params = {
        #         "shopId": "60",
        #         "shopType": "1",
        #         "name" : "接口测试教程3",
        #         "goodsCategoryId": "101",
        #         "goodsDesc": "这是商品详情描述(测试)",
        #         "location": "湖北省武汉市蔡甸区东合中心",
        #         "longitude": "114.98161105685764",
        #         "latitude": "30.9613623046875",
        #         "goodsSkuJsonList": """[{"goodsSpecAttributeList":[{"attributeName":"型号","attributeValue":"本","specAttributeId":"85"}],"inventory":"102","salePrice":"69","status":"1"}]""",
        #         "goodsSpecAttributeJsonList" : """[{"attributeName":"型号","attributeValue":"本","specAttributeId":"85"}]"""
        #         "pictureFileList":"",
        #         "videoFile": "",
        #
        #
        # }


        # data = {
        #             "current": "1",
        #         #             "currentMemberId": "56",
        #         #             "size": "30"
        #         # }

        response = requests.post(url=url,headers=headers,params=params)

        res = response.json()
        rest = jsonpath.jsonpath(res,"$...id")
        test =list(set(rest))
        print(res)
















































