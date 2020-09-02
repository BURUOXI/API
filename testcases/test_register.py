# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 19:46
# @Author  : felix
# @Email   : 876569085@qq.com
# @File    : test_register.py
# @Software: PyCharm

# import unittest
# import os
#
#
# from common.handlepath import DATADIR
# from common.readexcel import ReadExcel
# from common.handleconfig import conf
# from common.handlerandom import random_words,random_email,random_name
# from common.handlerequests import SendRequest
# from common.connectdb import DB
# from common.handlelog import log
# from library.ddt import ddt,data
#
#
#
#
#
# case_file = os.path.join(DATADIR,"apicases.xlsx")
#
#
# @ddt
# class TestRegister(unittest.TestCase):
#     excel = ReadExcel(case_file,"register")
#     cases = excel.read_data()
#     request = SendRequest()
#     db =DB()
#     # 读取excel用例数据
#
#
#     @data(*cases)   # 进行拆包
#     def test_register(self,case):
#         """注册的测试用例"""
#         # 第一步：准备用例数据
#
#         url = conf.get("evn","url") + case["url"]
#         headers = eval(conf.get("evn","headers"))
#         method = case["method"]
#         # 生成一个用户名
#         TestRegister.username = random_name().replace(" ","")
#         case["data"] = case["data"].replace("#username#", TestRegister.username)
#
#         # 随机生成一个邮箱
#         email = random_email()
#         case["data"] = case["data"].replace("#email#", email)
#
#         data = eval(case["data"])
#
#         expected = eval(case["expected"])
#         row = case["case_id"] + 1
#
#         #第二步：发送请求，获取结果
#         response = self.request.send(url=url, method=method, json=data, headers=headers)
#         res = response.json()
#         ses = response.status_code
#
#         # 第三步：断言，回写数据
#         try:
#             self.assertEqual(expected["status"], ses)
#             # self.assertEqual(expected["msg"], res["msg"])
#             # if case["check_sql"]:
#             #     sql = "SELECT username FROM test.auth_user WHERE username={}".format(TestRegister.username)
#             #     count=self.db.find_count(sql)
#             #     self.assertEqual(1, count)
#
#         except AssertionError as e:
#             self.excel.write_data(row=row, column=8, value="未通过")
#             log.error("用例：{}，执行未通过".format(case["title"]))
#             log.exception(e)
#             raise e
#         else:
#             self.excel.write_data(row=row, column=8, value="通过")
#             log.info("用例：{}，执行未通过".format(case["title"]))
#
#
#
#
#
#









































