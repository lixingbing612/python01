

# 存在的问题 ：
"""
1. 无法查看运行的用例数，比如成功几条，失败几条
2.如果失败 是什么导致的？最好给除失败的错误日志
3.无法去组织用例，不能控制哪些用例执行，哪些不执行
"""

# 解决方案 ： 使用unittest解决问题 测试框架 对用例分类套件 如 冒烟测试 回归测试

"""
unittest框架的功能： 
	1.unittest.TestCase()
	能对测试用例进行测试（断言）
	测试的结果能看到，及失败的原因
	可以进行初始化和清除功能
所编写的测试用例必须是一个类，且必须继承TestCase类
每个测试方法都是test开头
编写测试类建议Test开头
编写的模块建议小写test开头

	2.unittest.TestSuite()
	将不同的测试用例添加到不同的套件中
	a.可以添加不同的测试用例到套件中（单条）
	b.可以添加不同的测试用例组到套件中（一组）
	
	3.unittest.TestLoder()
	可以进行批量运行测试用例
	
	4.unittest.TextTestRunner()
	可以进行运行测试套件
"""
from project02.iter03_add_user import login		# 导入project02.iter03_add_user的方法login
import unittest		# 导入unittest类
import sys	#导入sys包


class TestLogin(unittest.TestCase):		# Testlogin继承unittest.TestCase类

	# 初始化类方法		setUpclass()	整个类在运行前，先运行setupClass()，只运行一次
	@classmethod
	def setUpClass(cls) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	# 清空类方法		tearDownclass()	整个类在运行结束时，先运行tearDownClass()，只运行一次
	@classmethod
	def tearDownClass(cls) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	# 初始化方法 ： setUp()			如果每次运行测试方法前都需要先执行setup()
	def setUp(self) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

	# 清空方法 ： tearDown()			如果每次运行测试方法后都需要先执行tearDown()
	def tearDown(self) -> None:
		print('开始运行方法：',sys._getframe().f_code.co_name)	# sys._getframe().f_code.co_name调用sys模块的函数

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
    unittest.main()

