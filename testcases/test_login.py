# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 17:12
# @Author  : felix
# @Email   : 876569085@qq.com
# @File    : test_login.py
# @Software: PyCharm



import unittest
import os


from common.handlepath import DATADIR
from common.readexcel import ReadExcel
from common.handleconfig import conf
from common.handlerandom import random_words,random_email
from common.handlerequests import SendRequest
from common.connectdb import DB
from common.handlelog import log
from library.ddt import ddt,data





case_file = os.path.join(DATADIR,"apicases.xlsx")


@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel(case_file,"login")
    cases = excel.read_data()
    request = SendRequest()
    db =DB()
    # 读取excel用例数据


    @data(*cases)   # 进行拆包
    def test_login(self,case):
        """登陆的测试用例"""
        # 第一步：准备用例数据

        url = conf.get("evn","url") + case["url"]
        headers = eval(conf.get("evn","headers"))
        method = case["method"]

        # 登陆账号使用配置文件里面预设值的
        TestLogin.mobile = eval(conf.get("test_data","mobile"))
        case["data"] = case["data"].replace("#mobile#", str(self.mobile))

        TestLogin.password = eval(conf.get("test_data", "password"))
        case["data"] = case["data"].replace("#password#", str(self.password))

        data = eval(case["data"])

        expected = eval(case["expected"])
        row = case["case_id"] + 1

        #第二步：发送请求，获取结果
        response = self.request.send(url=url, method=method, json=data, headers=headers)
        res = response.json()


        # 第三步：断言，回写数据
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])

        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="未通过")
            log.error("用例：{}，执行未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            log.info("用例：{}，执行未通过".format(case["title"]))























































