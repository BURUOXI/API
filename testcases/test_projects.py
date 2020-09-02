# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 19:42
# @Author  : felix
# @Email   : 876569085@qq.com
# @File    : test_projects.py
# @Software: PyCharm

import os
import unittest
import jsonpath
from common.handlepath import DATADIR
from common.readexcel import ReadExcel
from common.handlerequests import SendRequest
from common.handlelog import log
from common.handlerandom import random_name
from common.handleconfig import conf

from library.ddt import ddt,data

case_file = os.path.join(DATADIR,"apicases.xlsx")

@ddt
class TestProject(unittest.TestCase):
    excel = ReadExcel(case_file,"projects")
    cases = excel.read_data()
    request = SendRequest()


    @classmethod
    def setUpClass(cls) :
        # 1、准备登录的数据
        url = conf.get("evn", "url") + "/user/login/"
        data = {
            "username": eval(conf.get("test_data", "username")),
            "password": conf.get("test_data", "password")
        }
        headers = eval(conf.get("evn", "headers"))
        # 3、发送请求，进行登录
        response = cls.request.send(url=url, method="post", json=data, headers=headers)
        # 获取返回的数据
        res = response.json()
        # 3、提取token,保存为类属性
        # token = jsonpath.jsonpath(res, "token")[0]
        token = jsonpath.jsonpath(res, "token")[0]
        # 将提取到的token设为类属性
        cls.token_value = "JWT" + " " + token



    @data(*cases)
    def test_project(self,case):
        """新建项目接口"""
        # 第一步：准备用例数据
        url =   conf.get("evn","url") + case["url"]
        method = case["method"]
        headers = eval(conf.get("evn","headers"))
        headers["Authorization"] = self.token_value
        # 随机生成项目名
        name = random_name().replace(" ","")
        case["data"] = case["data"].replace("#name#", name)

        data= eval(case["data"])
        # 在请求头中加入setupclass中提取出来的token
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        #第二步：发送请求，获取结果
        response = self.request.send(url=url, method=method, json=data, headers=headers)
        res = response.json()
        ses = response.status_code

        # 第三步：断言（比对预期结果和实际结果）
        try:
            self.assertEqual(expected["status"], ses)

            # 判断示范需要进行sql校验
            # if case["check_sql"]:
            #     self.assertEqual(end_money - start_money, Decimal(str(data["amount"])))

        except AssertionError as e:
            print("预期结果：", expected)
            print("实际结果：", res)
            self.excel.write_data(row=row, column=8, value="未通过")
            log.error("用例：{}，执行未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            log.info("用例：{}，执行未通过".format(case["title"]))






































