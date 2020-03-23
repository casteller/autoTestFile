# import sys
# sys.path.append('.')
# from cheng_baby.element import *
# drvier=Test_ab()
# drvier.test_driver()
# drvier.driver.get("https://mail.163.com/")
# a=drvier.Get_attribute('tag_name','iframe','id')
# drvier.abc(a)
# drvier.test_element("css_selector","input[name='email']","13728659118")
# import sys
# sys.path.append('.')
# from lauchTime01.common import *
# drvier=Test_functions()
# drvier.test_driver('Chrome')
# drvier.driver.get('http://www.baidu.com')
# drvier.test_element("ById","kw","123")
import sys
sys.path.append('.')
from cheng_baby.element import *
import unittest
class Test_cc(unittest.TestCase): #必须要以Test开头
    def setUp(self):
        self.driver=Test_ab()
        self.driver.test_driver()
        self.driver.driver.get('http://www.baidu.com')
    def test_001(self):
        self.driver.test_element("id","kw","123")
        time.sleep(5)
        self.driver.test_elements("id",'su')
        time.sleep(5)
    def tearDown(self):
        self.driver.getout()
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Test_cc("test_001"))
