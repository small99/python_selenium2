# _*_ coding:utf-8 _*_

__author__ = '苦叶子'

import unittest
import sys

from selenium import webdriver
from pages.searchPage import SearchPage

reload(sys)
sys.setdefaultencoding("utf-8")


# 百度搜索测试
class TestSearchPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Ie()
        
    def testSearch(self):
        driver = self.driver
        # 百度网址
        url = u"http://www.baidu.com"
        # 搜索文本
        text = u"开源优测"
        # 期望验证的标题
        assert_title = u"开源优测_百度搜索"
        print assert_title
        
        search_Page = SearchPage(driver, url)
        
        # 启动浏览器，访问百度首页
        search_Page.gotoBaiduHomePage()
        
        # 输入 搜索词
        search_Page.input_search_text(text)
        
        # 单击 百度一下 按钮进行搜索
        search_Page.click_search_btn()
        
        # 验证标题
        self.assertEqual(search_Page.get_title(), assert_title)
        
    def tearDown(self):
        self.driver.quit()