#-*- coding:utf-8 -*-

__author__ = u'苦叶子'

from selenium import webdriver
import unittest
import HTMLTestRunner  
import sys
from time import sleep
import xlrd

reload(sys)
sys.setdefaultencoding("utf-8")

class LoadBaiduSearchTestData:
    def __init__(self, path):
        self.path = path
    
    def load_data(self):
        # 打开excel文件
        excel = xlrd.open_workbook(self.path)
        
        # 获取第一个工作表
        table = excel.sheets()[0]
        
        # 获取行数
        nrows = table.nrows
        
        # 从第二行开始遍历数据
        # 存入一个list中
        test_data = []
        for i in range(1, nrows):
            test_data.append(table.row_values(i))
        
        # 返回读取的数据列表    
        return test_data

class BaiduTest(unittest.TestCase):
    """百度首页搜索测试用例"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = u"http://www.baidu.com"
        self.path = u"baidu_search.xlsx"
        
    def test_baidu_search(self):
        driver = self.driver
        print u"开始[case_0001]百度搜索"
        
        
        # 加载测试数据
        test_excel = LoadBaiduSearchTestData(self.path)
        data = test_excel.load_data()
        print data
        
        # 循环参数化
        for d in data:
            # 打开百度首页
            driver.get(self.base_url)
            
            # 验证标题
            self.assertEqual(driver.title, u"百度一下，你就知道")
            sleep(1)
            
            driver.find_element_by_id("kw").clear()
            # 参数化 搜索词
            driver.find_element_by_id("kw").send_keys(d[1])
            sleep(1)
            driver.find_element_by_id("su").click()
            sleep(1)
            
            # 验证搜索结果标题
            self.assertEqual(driver.title, d[2])
            sleep(2)
            
        
    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(BaiduTest('test_baidu_search'))    
    # 定义报告输出路径
    htmlPath = u"testReport.html"
    fp = file(htmlPath, "wb")
    
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, 
           title=u"百度测试", 
           description=u"测试用例结果")
    
    runner.run(testunit)
    
    fp.close()