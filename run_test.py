# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 12:34
# @Author  : felix
# @Email   : 876569085@qq.com
# @File    : run_test.py
# @Software: PyCharm


import unittest
import os
from common.handlepath import CASEDIR,REPORTDIR
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.handle_email import send_email

# 第一步：创建套件
suite = unittest.TestSuite()

# 第二步：加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

report_file = os.path.join(REPORTDIR,"report1.html")

# 第三步：执行用例
runner = HTMLTestRunner(stream=open(report_file, "wb"),
                        description="接口测试报告",
                        title="app接口测试测试报告",
                        tester="谢谢谢"
                        )

runner.run(suite)

# 发送邮件
send_email(report_file,"自动化测试报告")















