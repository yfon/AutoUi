import os
import unittest

from BeautifulReport import BeautifulReport as bf

cases_path = '../test_cases'
# 通过类去执行testcase
report_path = '../report_file'
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass


def add_case(rule="*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(start_dir=cases_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


cases = add_case()

bf(cases).report(report_dir=report_path, description='测试了所有的测试用例')
