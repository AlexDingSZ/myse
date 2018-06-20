from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os

if __name__ == "__main__":
    case_path = os.path.join(os.getcwd(), "se")
    report_path = os.path.join(os.getcwd(), "report")
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.join(report_path,"auto_result_"+now+".html")
    report_file = open(report_path,"wb")

    runner= HTMLTestRunner(stream=report_file,title=u'自动化测试报告',description='执行测试结果')
    cases = unittest.defaultTestLoader.discover(case_path, pattern="my*.py", top_level_dir=None)
    runner.run(cases)
    wr.close()

