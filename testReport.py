#-*- coding:utf-8 -*-


__author__ = u'苦叶子'

from selenium import webdriver
import unittest
import HTMLTestRunner
import sys
from time import sleep

reload(sys)
sys.setdefaultencoding("utf-8")

class BaiduTest(unittest.TestCase):

    """百度首页搜索测试用例"""
    
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = u"http://www.baidu.com"
        
    def test_baidu_search(self):
        driver = self.driver
        
        print u"开始[case_0001]百度搜索"
        
        driver.get(self.base_url)
        
        self.assertEqual(driver.title, u"百度一下，你就知道")
        
        driver.find_element_by_id("kw").clear()
        
        driver.find_element_by_id("kw").send_keys(u"开源优测")
        
        driver.find_element_by_id("su").click()
        
        sleep(3)
        
        self.assertEqual(driver.title, u"开源优测_百度搜索")
        
    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(BaiduTest('test_baidu_search'))
    
    # 定义报告输出路径
    htmlPath = u"D:\\testReport.html"
    fp = file(htmlPath, "wb")
    
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试", description=u"测试用例结果")
    
    runner.run(testunit)
    
    fp.close()