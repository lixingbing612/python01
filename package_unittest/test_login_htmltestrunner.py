


# 问题 ： 用unitest的测试报告太简单，只能在控制台查看，想生成的测试报告能更详细，能在浏览器中打开

# 解决方案 : 使用HTMLTestRunner模块生成测试报告 ， 原理 ： 将运行的测试用例结果输出到html文件中 就能使用浏览器打开

# 类 ：HTMLTestRunner(f,title,description)
#		f : 是指文件对象，一般是HTML文件
# 		title ： 生成测试报告标题
#		description ： 生成测试报告的描述

from project02.iter03_add_user import login		# 导入project02.iter03_add_user的方法login
import unittest		# 导入unittest类
import sys	#导入sys包
from package_unittest.HTMLTestRunner import HTMLTestRunner  # 导入测试报告包的HTMLTestRunner类


class TestLogin(unittest.TestCase):		# Testlogin继承unittest.TestCase类


	# 1.测试登录的测试用例

	# case1 ：输入正确用户名和密码
	def test_login_success(self):
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 0 	# 预期结果是0
		actual_value = login('admin','123456').get('code')	# 实际结果 需导入登录方法 alt+enter，调用project02.iter03_add_user的login模块
		self.assertEqual(except_value,actual_value)	# self调用unittest_TestCase的方法，断言期望值是不是和实际值相等，如果相等会输出结果

	# case2 ：输入错误的用户名或密码
	def test_user_wrong(self):
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 1 	# 预期结果是1
		actual_value = login('aaaaa','123456').get('code')	# 实际结果 需导入登录方法 alt+enter，调用project02.iter03_add_user的login模块
		self.assertEqual(except_value,actual_value)	# self调用unittest_TestCase的方法，断言期望值是不是和实际值相等，如果相等会输出结果

	# case3 ： 输入空的用户名或密码
	def test_password_is_null(self):
		print('开始运行方法：',sys._getframe().f_code.co_name)
		except_value = 1 	# 预期结果是1
		actual_value = login('admin',' ').get('code')	# 实际结果与预期结果不符合，输出结果，调用project02.iter03_add_user的login模块
		self.assertEqual(except_value,actual_value)	# self调用unittest_TestCase的方法，断言期望值是不是和实际值相等，如果相等会输出结果

if __name__ == '__main__':

	# 创建一个套件a
	suite_a = unittest.TestSuite()		# 调用unittest的TestSuite
	suite_a.addTest(TestLogin('test_login_success'))		# 调用addTest方法将测试用例TestLogin类test_login_success的方法添加到套件suite_a
	suite_a.addTest(TestLogin('test_user_wrong'))		# 调用addTest方法将测试用例TestLogin类test_user_wrong的方法添加到套件suite_a
	suite_a.addTest(TestLogin('test_password_is_null'))		# 调用addTest方法将测试用例TestLogin类test_user_wrong的方法添加到套件suite_a
	print(suite_a)

	# 创建测试报告文件，是HTML格式
	test_report = './test_report.html'	# 设置报告生成路径和文件名

	with open(test_report,'wb') as f:	# 打开报告

		runner = HTMLTestRunner(f, title='测试报告', description="测试报告描述") # 调用生成测试报告
		runner.run(suite_a)	# runner调用run()方法
